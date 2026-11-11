import sys
import re
import json
import ssl
import urllib.request
import urllib.error
import os

SSL_CTX = ssl.create_default_context()
SSL_CTX.check_hostname = False
SSL_CTX.verify_mode = ssl.CERT_NONE


GRAPHQL_URL = "https://leetcode.com/graphql"

QUERY = """
query getProblem($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    questionFrontendId
    title
    titleSlug
    difficulty
    content
    codeSnippets {
      lang
      langSlug
      code
    }
  }
}
"""

SEARCH_QUERY = """
query problemsetQuestionList($skip: Int, $limit: Int, $filters: QuestionListFilterInput) {
  problemsetQuestionList: questionList(
    categorySlug: ""
    limit: $limit
    skip: $skip
    filters: $filters
  ) {
    questions: data {
      frontendQuestionId: questionFrontendId
      titleSlug
      title
    }
  }
}
"""


def graphql(query, variables):
    payload = json.dumps({"query": query, "variables": variables}).encode()
    req = urllib.request.Request(
        GRAPHQL_URL,
        data=payload,
        headers={
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0",
            "Referer": "https://leetcode.com",
        },
    )
    with urllib.request.urlopen(req, timeout=15, context=SSL_CTX) as resp:
        return json.loads(resp.read())


def search_questions(keyword: str, limit: int = 50) -> list:
    data = graphql(
        SEARCH_QUERY,
        {"limit": limit, "skip": 0, "filters": {"searchKeywords": keyword}},
    )
    return data["data"]["problemsetQuestionList"]["questions"]


def find_slug_by_number(number: int) -> str:
    questions = search_questions(str(number), limit=50)
    for q in questions:
        if int(q["frontendQuestionId"]) == number:
            return q["titleSlug"]
    raise SystemExit(f"Challenge #{number} not found on LeetCode.")


def normalize_title(title: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", title.lower()).strip()


def find_slug_by_title(title: str) -> str:
    title = title.strip()
    questions = search_questions(title)
    if not questions:
        raise SystemExit(f"No LeetCode challenge found for '{title}'.")

    wanted = normalize_title(title)
    exact = [q for q in questions if normalize_title(q["title"]) == wanted]
    if exact:
        return exact[0]["titleSlug"]

    print(f"No exact title match for '{title}'. Possible results:")
    for index, question in enumerate(questions[:10], start=1):
        print(f"  {index}. {question['title']} (#{question['frontendQuestionId']})")
    raise SystemExit(
        "Search stopped to avoid creating a different challenge. "
        "Use the exact LeetCode title or its number."
    )


def html_to_text(html: str) -> str:
    html = re.sub(r"<br\s*/?>", "\n", html, flags=re.IGNORECASE)
    html = re.sub(r"<p>", "\n", html, flags=re.IGNORECASE)
    html = re.sub(r"</p>", "\n", html, flags=re.IGNORECASE)
    html = re.sub(r"<li>", "\n- ", html, flags=re.IGNORECASE)
    html = re.sub(r"<[^>]+>", "", html)
    html = html.replace("&lt;", "<").replace("&gt;", ">").replace("&amp;", "&")
    html = html.replace("&nbsp;", " ").replace("&#39;", "'").replace("&quot;", '"')
    return re.sub(r"\n{3,}", "\n\n", html).strip()


def get_python_snippet(snippets: list) -> str:
    for s in snippets:
        if s["langSlug"] == "python3":
            return s["code"]
    return "class Solution:\n    def solve(self) -> None:\n        pass\n"


def get_example_calls(description: str, method_name: str) -> str:
    """Create runnable calls from LeetCode lines such as: Input: nums = [1,2,2]."""
    calls = []
    for match in re.finditer(r"^Input:\s*(.+)$", description, flags=re.MULTILINE):
        input_text = match.group(1).strip()
        # Split only between assignments, not commas inside lists or strings.
        assignments = re.split(r",\s*(?=[A-Za-z_]\w*\s*=)", input_text)
        arguments = []
        for assignment in assignments:
            name, separator, value = assignment.partition("=")
            if not separator or not re.fullmatch(r"\s*[A-Za-z_]\w*\s*", name):
                arguments = []
                break
            arguments.append(f"{name.strip()}={value.strip()}")
        if arguments:
            calls.append(f"solution.{method_name}({', '.join(arguments)})")

    if not calls:
        return ""
    return "\n\n\nsolution = Solution()\n" + "\n".join(calls) + "\n"


def parse_number(arg: str):
    match = re.search(r"\d+", arg)
    return int(match.group()) if match else None


def main():
    if len(sys.argv) < 2:
        print("Usage: python get_challenge.py <number|title>")
        print("  e.g. python get_challenge.py 1")
        print('  e.g. python get_challenge.py "Two Sum"')
        sys.exit(1)

    search = " ".join(sys.argv[1:]).strip()
    number = parse_number(search)
    if number is not None and search.replace(str(number), "", 1).strip() == "":
        print(f"Fetching challenge #{number}...")
        slug = find_slug_by_number(number)
    else:
        print(f"Searching LeetCode for '{search}'...")
        slug = find_slug_by_title(search)

    data = graphql(QUERY, {"titleSlug": slug})
    q = data["data"]["question"]

    folder_name = f"{int(q['questionFrontendId']):04d}-{q['titleSlug']}"
    folder_path = os.path.join(os.getcwd(), folder_name)

    if os.path.exists(folder_path):
        raise SystemExit(f"Folder '{folder_name}' already exists.")

    os.makedirs(folder_path)

    # README
    description = html_to_text(q["content"]) if q["content"] else "No description available."
    readme = f"# {q['questionFrontendId']}. {q['title']}\n\n"
    readme += f"**Difficulty:** {q['difficulty']}\n\n"
    readme += f"**LeetCode:** https://leetcode.com/problems/{q['titleSlug']}/\n\n"
    readme += f"## Problem\n\n{description}\n"

    with open(os.path.join(folder_path, "README.md"), "w", encoding="utf-8") as f:
        f.write(readme)

    # solution.py
    snippet = get_python_snippet(q["codeSnippets"])
    method_match = re.search(r"^\s*def\s+(\w+)\s*\(", snippet, flags=re.MULTILINE)
    if method_match:
        if snippet.rstrip().endswith(":"):
            snippet = snippet.rstrip() + "\n        pass\n"
        snippet += get_example_calls(description, method_match.group(1))
    with open(os.path.join(folder_path, "solution.py"), "w", encoding="utf-8") as f:
        f.write(snippet + "\n")

    print(f"Created: {folder_name}/")
    print(f"  - README.md")
    print(f"  - solution.py")


if __name__ == "__main__":
    main()
