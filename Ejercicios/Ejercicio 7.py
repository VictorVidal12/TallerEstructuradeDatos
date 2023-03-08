def printArr(arr, n):
    for i in range(n):
        print(arr[i], " ", end="")
    print()


''' Function to generates and prints all
    sorted arrays from alternate elements of
   'A[i..m-1]' and 'B[j..n-1]'
   If 'flag' is true, then current element
   is to be included from A otherwise
   from B.
   'len' is the index in output array C[].
    We print output  array  each time
   before including a character from A
   only if length of output array is
   greater than 0. We try than all possible combinations '''


def generateUtil(A, B, C, i, j, m, n, len, flag):
    if (flag):
        if (len):
            printArr(C, len + 1)
        for k in range(i, m):
            if (not len):
                C[len] = A[k]
                generateUtil(A, B, C, k + 1, j, m, n, len, not flag)
            else:
                if (A[k] > C[len]):
                    C[len + 1] = A[k]
                    generateUtil(A, B, C, k + 1, j, m, n, len + 1, not flag)
    else:
        for l in range(j, n):
            if (B[l] > C[len]):
                C[len + 1] = B[l]
                generateUtil(A, B, C, i, l + 1, m, n, len + 1, not flag)

def generate(A, B, m, n):
    C = []
    for i in range(m + n + 1):
        C.append(0)
    generateUtil(A, B, C, 0, 0, m, n, 0, True)

A = [10, 15, 25]
B = [5, 20, 30]
n = len(A)
m = len(B)

generate(A, B, n, m)