arr = input("Enter the list of numbers seperated by spaces: ").split(", ")
arr = [int(x) for x in arr]

target = int(input("Enter the target value to search: "))
found = False
for i in range(len(arr)):
    if arr[i] == target:
        print(f"Target {target} found at index {i}.")
        found = True

if not found:
    print(f"Target {target} not found in the array.")