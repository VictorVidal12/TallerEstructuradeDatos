def atoiRecursive(string, num):
    if string.isalpha():
        return 0
    if (len(string) == 0):
        return 0
    if len(string) == 1:
        return int(string) + (num * 10)
    num = int(string[0:1]) + (num * 10)
    return atoiRecursive(string[1:], num)



string = "0123456789"

print(atoiRecursive(string, 0))