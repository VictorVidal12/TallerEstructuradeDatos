class Palindromes:
    def palindromos(self, arr):
        self.res.add(tuple(arr))
        if len(arr)<=1:
            return
        for i in range(1,len(arr)):
            if arr[i-1]==arr[i][::-1]:
                brr = arr[:i-1] + [arr[i-1]+arr[i]] + arr[i+1:]
                self.palindromos(brr)
            if i+1<len(arr) and arr[i-1]==arr[i+1][::-1]:
                brr = arr[:i-1] + [arr[i-1]+arr[i]+arr[i+1]] + arr[i+2:]
                self.palindromos(brr)
    def getGray(self, S):
        self.res = set()
        self.palindromos(list(S))
        return sorted(list(self.res))


ob = Palindromes()
allPart = ob.getGray("Ana lava lana")
for i in range(len(allPart)):
    for j in range(len(allPart[i])):
        print(allPart[i][j], end = " ")
    print()
