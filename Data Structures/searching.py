# Binary Search 
def binarySearch(arr, target):
  left = 0
  right = len(arr) - 1

  while left <= right:
    mid = (left + right) // 2

    if arr[mid] == target:
      return mid

    if arr[mid] < target:
      left = mid + 1
    else:
      right = mid - 1

  return -1

mylist = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
x = 11

result = binarySearch(mylist, x)

if result != -1:
  print("Found at index", result)
else:
  print("Not found")


# Linear search
key=int(input())
search_list=list(map(int, input().split()))
for i in len(search_list):
    if key == search_list[i]:
        print(f'key was found in the index {i}')
        break
else:
    print('the key was not found')


# Binary search using recurssion
def binary_search_rec(arr, target, left, right):
    if left > right:  
        return -1
    
    mid = (left + right) // 2
    
    if arr[mid] == target:
        return mid
    elif target < arr[mid]:
        return binary_search_rec(arr, target, left, mid - 1)
    else:
        return binary_search_rec(arr, target, mid + 1, right)


my_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
left = 0
right = len(my_list) - 1
target = int(input("Enter the target you want to be searched: "))

result = binary_search_rec(my_list, target, left, right)

if result != -1:
    print("Found at index", result)
else:
    print("Not found")
