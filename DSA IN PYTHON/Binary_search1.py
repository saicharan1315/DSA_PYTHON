def first_occ(arr, n, key):
    s, e = 0, n - 1
    ans = -1
    while s <= e:
        mid = s + (e - s) // 2
        if arr[mid] == key:
            ans = mid
            e = mid - 1
        elif key > arr[mid]:
            s = mid + 1
        else:
            e = mid - 1
    return ans

def last_occ(arr, n, key):
    s, e = 0, n - 1
    ans = -1
    while s <= e:
        mid = s + (e - s) // 2
        if arr[mid] == key:
            ans = mid
            s = mid + 1
        elif key > arr[mid]:
            s = mid + 1
        else:
            e = mid - 1
    return ans

def first_and_last_position(arr, k):
    n = len(arr)
    first = first_occ(arr, n, k)
    last = last_occ(arr, n, k)
    return (first, last)

# Example usage
arr = [1, 2, 2, 3, 3, 3, 4, 5, 5]
k = 3
result = first_and_last_position(arr, k)
print(f"First and last position of {k}: {result}")