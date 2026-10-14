def merge_sort(list: list[int]) -> list[int]:
    if len(list) <= 1:
       return list

    mid = len(list) // 2
    left = list[:mid]
    right = list[mid:]

    # recursive call to divide the halves until the base case is reached.
    left = merge_sort(left)
    right = merge_sort(right)

    # join the two ordered halves.
    return merge(left, right)

def merge(left, right):
    result = []
    pll = 0 
    prl = 0

    while pll < len(left) and prl < len(right):
        if left[pll] < right[prl]:
            result.append(left[pll])
            pll += 1
        else:
            result.append(right[prl])
            prl += 1
    result.extend(left[pll:])
    result.extend(right[prl:])
    
    return result

merge_sort([5,4,3,2,1])
merge_sort([1,3,4,5,2])

