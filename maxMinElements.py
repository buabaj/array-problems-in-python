def maxMinElements(arr):
    max = arr[0]
    min = arr[0]
    for i in range(len(arr)):
        if arr[i] > max:
            max = arr[i]
        if arr[i] < min:
            min = arr[i]
    return max, min


print(maxMinElements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
