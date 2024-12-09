def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

arr = [15, 78, 65, 23, 41, 12, 7, 36]
print("Before sorted: ", arr)
sorted_array = quick_sort(arr)
print("After sorted: ", sorted_array)
# O(n log n)