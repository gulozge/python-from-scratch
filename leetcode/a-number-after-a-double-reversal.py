class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        num = str(num)
        if num[-1] != "0" or num[0] == "0":
            return True
        else:
            return False


solution = Solution()
print(solution.isSameAfterReversals(501))
