class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            tmp = 0
            str_n = str(n)
            for i in str_n:
                tmp += int(i) ** 2
            n = tmp
        return True


solution = Solution()
print(solution.isHappy(2))
