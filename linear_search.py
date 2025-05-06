def linear_search(arr, target):
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i
    return -1
my_list = [1,56,2,3,4,7,57,99,11]
print(linear_search(my_list, 70))    
print(linear_search(my_list, 7))
    
