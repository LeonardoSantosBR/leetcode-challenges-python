def selection_sort(list: list[int]) -> list[int]:
     size = len(list)
     
     for i in range(size):
        lower_index = i
        
        for j in range(i + 1, size):
            if list[j] < list[lower_index]:
                lower_index = j
        if lower_index != i:
            list[i], list[lower_index] = list[lower_index], list[i]
     return list
            
selection_sort([5,4,3,2,1])
selection_sort([1,3,4,5,2])