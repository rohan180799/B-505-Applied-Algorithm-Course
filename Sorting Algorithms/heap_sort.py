def maxheapify(arr, n, i):
    largest = i
    l = 2*i
    r = 2*i + 1

    while l < n and arr[l] > arr[largest]:
        largest = l
    while r < n and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        maxheapify(arr, n, largest)

def heapsort(arr):
    n = len(arr)

    for i in range(n//2 - 1, -1, -1):
        maxheapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        maxheapify(arr, i, 0)

arr = [12, 11, 13, 5, 6, 7]
heapsort(arr)
n = len(arr)
print("Sorted array is")
for i in range(n):
    print("%d" % arr[i]),
