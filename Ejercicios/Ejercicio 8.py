def first(word):
    for i in range(0, len(word)):
        if (word[i].isupper()):
            return word[i]
    return "No contiene mayúscula"

word = "pArangaricutirimicuaro"
print(first(word))