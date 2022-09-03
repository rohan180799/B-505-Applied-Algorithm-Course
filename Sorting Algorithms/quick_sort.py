def partition(arr, start, end):
    pivot_index = start
    pivot = arr[pivot_index]

    while start < end:
        while start < len(arr) and arr[start] <= pivot:
            start += 1
        while arr[end] > pivot:
            end -= 1
        if start < end:
            arr[start], arr[end] = arr[end], arr[start]

    arr[end], arr[pivot_index] = arr[pivot_index], arr[end]
    return end


def quicksort(arr, start, end):
    if start < end:
        p = partition(arr, start, end)

        quicksort(arr, start, p - 1)
        quicksort(arr, p + 1, end)


if __name__ == "__main__":
    a = [1, 4, 7, 2, 8, 3]

    quicksort(a, 0, len(a) - 1)

    print (a)
