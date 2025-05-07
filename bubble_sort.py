def bubble_sort(arr):
    n = len(arr)
    for passes in range(n-1):
        for j in range(0, (n-1) - passes): #beacuse indexing start from zero go till the 5 i means total len - 1 
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr        





unsorted_list = [7,23,2,123,88,666,99]
sorted_list = bubble_sort(unsorted_list)
print("Sorted list:",sorted_list)
list2 = [1,66,4,65,0]
print("orginal list:", list2)
print(bubble_sort(list2))
print(bubble_sort([]))
