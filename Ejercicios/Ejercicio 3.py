def generateAllStringsUtil(K, str, n):
    if (n == K):
        print(*str[:n], sep="", end=" ")
        return

    if (str[n - 1] == '1'):
        str[n] = '0'
        generateAllStringsUtil(K, str, n + 1)

    if (str[n - 1] == '0'):
        str[n] = '0'
        generateAllStringsUtil(K, str, n + 1)
        str[n] = '1'
        generateAllStringsUtil(K, str, n + 1)

def generateAllStrings(K):
    if (K <= 0):
        return
    str = [0] * K
    str[0] = '0'
    generateAllStringsUtil(K, str, 1)
    str[0] = '1'
    generateAllStringsUtil(K, str, 1)

K = 3
generateAllStrings(K)