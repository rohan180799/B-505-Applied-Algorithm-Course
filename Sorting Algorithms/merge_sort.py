def mergesort(arr):
    if len(arr) > 1:

        mid = len(arr) // 2

        L = arr[:mid]
        R = arr[mid:]
        mergesort(L)
        mergesort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def printList(arr):
    for i in range(len(arr)):
        print(arr[i])


if __name__ == "__main__":
    a = [9, 3, 4, 5, 6, 27, 45, 87, 0, 13, 51]
    mergesort(a)
    printList(a)
