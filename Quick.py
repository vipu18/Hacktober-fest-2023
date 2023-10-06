def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def binary_search(arr, low, high, key):
    if high >= low:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            return binary_search(arr, low, mid - 1, key)
        else:
            return binary_search(arr, mid + 1, high, key)
    else:
        return -1

size = int(input("Enter size of array: "))
arr = []
for i in range(size):
    element = int(input("Enter element no {}: ".format(i + 1)))
    arr.append(element)

quick_sort(arr, 0, size - 1)

print("Sorted array:", arr)

key = int(input("Enter key: "))
result = binary_search(arr, 0, size - 1, key)

if result != -1:
    print("Key is found at index", result)
else:
    print("Key not found")
