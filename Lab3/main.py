def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def sink(arr, i, n):
    k = i
    comparisons = 0
    assignments = 0

    while True:
        j = 2 * k + 1
        if j >= n:
            break

        comparisons += 1
        if j + 1 < n and arr[j + 1] > arr[j]:
            j += 1

        comparisons += 1
        if arr[k] >= arr[j]:
            break

        swap(arr, k, j)
        assignments += 3
        k = j

    return comparisons, assignments


def heapsort(arr):
    n = len(arr)
    total_comparisons = 0
    total_assignments = 0

    # Phase 1: Build max heap
    for i in range(n // 2 - 1, -1, -1):
        c, a = sink(arr, i, n)
        total_comparisons += c
        total_assignments += a

    # Phase 2: Sort
    for i in range(n - 1, 0, -1):
        swap(arr, 0, i)
        total_assignments += 3
        c, a = sink(arr, 0, i)
        total_comparisons += c
        total_assignments += a

    return arr, total_comparisons, total_assignments
