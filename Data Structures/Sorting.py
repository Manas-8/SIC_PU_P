# Bubble Sort
def bubble_sort(arr):
    size=len(arr)
    for i in range(size-1):
        swapped=False
        for j in range(size-i-1):
            if arr[j] > arr[j+1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
                swapped=True
        if not swapped:
            break
    print(arr)

my_list = [64, 34, 25, 12, 22, 11, 90, 5]
bubble_sort(my_list)


# Selection Sort
def selection_sort(arr):
    size=len(arr)
    for i in range(size):
        min = i
        for j in range(i+1, size):
            if arr[min] > arr[j]:
                min = j
        arr[min], arr[i] = arr[i], arr[min]

    return arr

my_list = [64, 34, 25, 12, 22, 11, 90, 5]
print(selection_sort(my_list))


# Quick Sort
def partition(arr, low, high):
    pivot = arr[high]
    k = low - 1
    
    for j in range(low, high):
        if arr[j] < pivot:
            k+=1
            arr[k], arr[j] = arr[j], arr[k]
    arr[k+1], arr[high] = arr[high], arr[k+1]
    return k+1
        
def quick_sort(arr, low=0, high=None):
    if high == None:
        high = len(arr) - 1
        
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)
        
    
my_list=[34,67,45,23,5,65,12,39,28]
quick_sort(my_list)
print(my_list)
