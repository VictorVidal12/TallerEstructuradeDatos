def printArr(arr, k):
    for i in range(k):
        print(arr[i], end=" ")
    print()

def printSeqUtil(n, k, len1, arr):

    if (len1 == k):
        printArr(arr, k)
        return

    i = 1 if (len1 == 0) else (arr[len1 - 1] + 1)

    len1 += 1

    while (i <= n):
        arr[len1 - 1] = i
        printSeqUtil(n, k, len1, arr)
        i += 1

    len1 -= 1

def printSeq(n, k):
    arr = [0] * k
    len1 = 0
    printSeqUtil(n, k, len1, arr)

k = 3
n = 7
printSeq(n, k)