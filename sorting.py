# Description: This file contains the implementation of various sorting algorithms.


def selection_sort(arr, ascending=True): # O(n^2) time complexity and O(1) space complexity 
    n = len(arr)
    for i in range(n):
        extrema_index = i
        for j in range(i + 1, n):
            if (ascending and arr[j] < arr[extrema_index]) or (not ascending and arr[j] > arr[extrema_index]):
                extrema_index = j
        arr[i], arr[extrema_index] = arr[extrema_index], arr[i]
    return arr

def bubble_sort(arr, ascending=True): # O(n^2) time complexity and O(1) space complexity 
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if (ascending and arr[j] > arr[j + 1]) or (not ascending and arr[j] < arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def insertion_sort(arr, ascending=True): # O(n^2) time complexity and O(1) space complexity
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and ((ascending and key < arr[j]) or (not ascending and key > arr[j])):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def merge_sort(arr, ascending=True): # O(nlogn) time complexity and O(n) space complexity 
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L, ascending)
        merge_sort(R, ascending)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if (ascending and L[i] < R[j]) or (not ascending and L[i] > R[j]):
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
    return arr

def quick_sort(arr, ascending=True): # O(nlogn) time complexity and O(logn) space complexity
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if (ascending and x < pivot) or (not ascending and x > pivot)]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if (ascending and x > pivot) or (not ascending and x < pivot)] 
    return quick_sort(left, ascending) + middle + quick_sort(right, ascending)


def heap_sort(arr, ascending=True): # O(nlogn) time complexity and O(1) space complexity
    def heapify(arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and ((ascending and arr[i] < arr[l]) or (not ascending and arr[i] > arr[l])):
            largest = l
        if r < n and ((ascending and arr[largest] < arr[r]) or (not ascending and arr[largest] > arr[r])):
            largest = r
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr

def comb_sort(arr, ascending=True): # O(n^2) time complexity and O(1) space complexity
    n = len(arr)
    gap = n
    shrink = 1.3
    swapped = True
    while gap > 1 or swapped:
        gap = int(gap / shrink)
        if gap < 1:
            gap = 1
        swapped = False
        for i in range(n - gap):
            if (ascending and arr[i] > arr[i + gap]) or (not ascending and arr[i] < arr[i + gap]):
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                swapped = True
    return arr
