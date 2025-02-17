class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        if str_x[::-1] == str_x[0:]:
            return True
        else:
            return False


solution = Solution()
print(solution.isPalindrome(121))
