def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]

        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

my_list = [21, 43, 10, 76, 84, 74, 99, 65]

print("Original List:", my_list)
insertion_sort(my_list)
print("Sorted List:", my_list)