def binary_search(list: list[int], n: int) -> int:
    list.sort()
    lo=0
    hi=len(list)
    
    while lo < hi:
        mid = int((lo+hi)/2)
        if list[mid] == n:
            return n
        elif list[mid] < n:
            lo = mid+1
        else:
            hi = mid
    return -1
          
binary_search([4,5,2,3,6,9,1],3)