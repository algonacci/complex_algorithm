def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        
        elif arr[mid] > target:
            right = mid - 1

        else:
            left = mid + 1

    return -1


arr = [15, 78, 65, 23, 41, 12, 7, 36]
arr.sort()
target = 41
result = binary_search(arr, target)

if result != -1:
    print(f"Target {target} ditemukan di indeks {result}")
else:
    print(f"Target {target} tidak ditemukan dalam array")
