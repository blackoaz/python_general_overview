import time
def insertion_sort():
    A = [5, 2, 4, 6, 1, 3]
    # A = [31, 41, 59, 26, 41, 58]
    n = len(A)
    starttime = time.time()
    for i in range(1,n):
        
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = key
    endtime = time.time()
    print(endtime - starttime)
    print(A)

insertion_sort()


def insertion_sort_descending():
    A = [5, 2, 4, 6, 1, 3]
    n = len(A)
    for i in range(1, n):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] < key:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = key
    print(A)

#insertion_sort_descending()








