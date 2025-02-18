class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if a == "0" and b == "0":
            return "0"
        if len(a) > len(b):
            sub = len(a) - len(b)
            b = '0' * sub + b
        else:
            sub = len(b)-len(a)
            a = '0' * sub + a

        tmp = ""
        e = 0
        i = len(a)-1

        while i >= 0:
            add = int(a[i])+int(b[i])+e
            if add == 2:
                tmp = "0" + tmp
                e = 1
            elif add == 3:
                tmp = "1" + tmp
                e = 1
            else:
                tmp = str(add)+tmp
                e = 0
            i = i-1
        if e == 1:
            tmp = "1"+tmp
        return tmp


solution = Solution()
print(solution.addBinary("1010", "1011"))
