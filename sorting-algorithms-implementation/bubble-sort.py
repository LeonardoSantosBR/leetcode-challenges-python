def bubble_sort(list: list[int]):
    size = len(list)
    
    for _ in list:
        is_sorted = True
        for i in range(size-1):
            if list[i] > list[i+1]:
                is_sorted = False
                list[i+1], list[i] = list[i] , list[i+1]
        if is_sorted:
            return
            

bubble_sort([5,4,3,2,1])
bubble_sort([1,3,4,5,2])