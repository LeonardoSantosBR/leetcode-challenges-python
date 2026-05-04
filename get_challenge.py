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


def find_slug_by_number(number: int) -> str:
    data = graphql(
        SEARCH_QUERY,
        {"limit": 1, "skip": 0, "filters": {"searchKeywords": str(number)}},
    )
    questions = data["data"]["problemsetQuestionList"]["questions"]
    for q in questions:
        if int(q["frontendQuestionId"]) == number:
            return q["titleSlug"]
    raise SystemExit(f"Challenge #{number} not found on LeetCode.")


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


def parse_arg(arg: str) -> int:
    match = re.search(r"\d+", arg)
    if not match:
        raise SystemExit(f"Could not parse challenge number from '{arg}'")
    return int(match.group())


def main():
    if len(sys.argv) < 2:
        print("Usage: python get_challenge.py <number>")
        print("  e.g. python get_challenge.py 1")
        sys.exit(1)

    number = parse_arg(sys.argv[1])
    print(f"Fetching challenge #{number}...")

    slug = find_slug_by_number(number)
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
    with open(os.path.join(folder_path, "solution.py"), "w", encoding="utf-8") as f:
        f.write(snippet + "\n")

    print(f"Created: {folder_name}/")
    print(f"  - README.md")
    print(f"  - solution.py")


if __name__ == "__main__":
    main()
