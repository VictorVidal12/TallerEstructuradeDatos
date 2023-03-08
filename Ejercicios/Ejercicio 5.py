def printTriangle(x):
    if (len(x) == 1):
        return
    temp = [0] * (len(x) - 1)
    helper(temp, x, 0)
    printTriangle(temp)
    print(temp)

def helper(temp, x, index):
    if (index == len(x) - 1):
        return temp
    temp[index] = x[index] + x[index + 1]
    return helper(temp, x, index + 1)


x = [1, 2, 3, 4, 5]
printTriangle(x)
print(x)