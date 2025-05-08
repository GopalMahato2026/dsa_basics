def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr            




my_list = [122,34,345,2,234,5,23,2]
print("Normal version: ",my_list)
print("Sorted version: ",selection_sort(my_list))