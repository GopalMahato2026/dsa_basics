def binary_search(arr, target):
    low = 0
    high = len(arr) - 1 
    while low <= high:
        mid = (low + high) // 2 #finding the middle index
        guess = arr[mid]
        if guess == target:
            return mid # target found return its index
        elif guess > target:
            high = guess - 1
        elif guess < target:
            low = guess + 1
    return -1
#example usage:
numbers = [1,3,5,7,9,11,13,15] 
target = 7
result = binary_search(numbers, target)
if result != -1:           
    print(f"Found at index {result}")
else:
    print("Not found!")    


        
