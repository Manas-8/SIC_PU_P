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
