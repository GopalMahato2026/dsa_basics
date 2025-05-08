#what type of sorting and searching algorithm program i learned
#fisrt one is linear search a very basic searching algorithm
#In this way this function loop through every element of the list/array, list don't need to be sorted!
def linear_search(arr, target):
    for i in range(0,len(arr)):
        if arr[i] == target:
            return i
    return -1

my_list = [1,2,4,34,3,7,5]
print(linear_search(my_list, 34))

#lets practiceing binary search
#in this way list need to be sorted 
def binary_search(arr, target):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        elif arr[mid] > target:
            end = mid - 1



    return -1

my_list2 = [12, 23, 34, 42, 65, 66, 98, 345]
print(binary_search(my_list2, 345))   

### making sorting algorithm
## bubble sort
def bubble_sort(arr):
    for passes in range(len(arr) - 1):
        for j in range(0,((len(arr))- 1) - passes):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

my_list3 = [1,34,776,34,34,98,43,77]
print(bubble_sort(my_list3))



### lets  trying the selection sort way 


##fiding min element 
def min_find(arr):
    min_element = 1000000
    for i in arr:
        if i < min_element:
            min_element = i

    return min_element
my_list = [1,2,45,33,234,532,3,-1,9]        
print(f"List: {my_list}\nMin Element: {min_find(my_list)}")


