def printCombinations(input, index, output, outLength):
    if (len(input) == index):
        output[outLength] = '\0'
        print(*output[:outLength], sep="")
        return

    output[outLength] = input[index]

    output[outLength + 1] = ' '
    printCombinations(input, index + 1,
                      output, outLength + 2)

    if (len(input) != (index + 1)):
        printCombinations(input, index + 1,
                          output, outLength + 1)



input = "12345"
output = [0] * 100

output[0] = '\0'

printCombinations(input, 0, output, 0)