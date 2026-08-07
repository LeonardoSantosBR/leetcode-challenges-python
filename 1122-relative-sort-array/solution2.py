class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        rank = {v: i for i, v in enumerate(arr2)} #*bubble sort*
        big = len(arr2)
        n = len(arr1)

        for i in range(n - 1):
            swapped = False
            for j in range(n - 1 - i):
                a, b = arr1[j], arr1[j + 1]
                if (rank.get(a, big), a) > (rank.get(b, big), b):
                    arr1[j], arr1[j + 1] = arr1[j + 1], arr1[j]
                    swapped = True
            if not swapped:
                break
        return arr1

solution = Solution()
solution.relativeSortArray([2,3,1,3,2,4,6,7,9,2,19],[2,1,4,3,9,6])

# • Sua solução: O(n²) tempo — O(m) espaço, via bubble sort com chave (rank, valor).
# • Sugerido: O(n + k) tempo — O(k) espaço, via counting sort (ver solution.py).