class Solution:
    def sumBase(self, n: int, k: int) -> int:
        result = 0
        while n != 0:
            result = result+n % k
            n = n//k
        return result


solution = Solution()
print(solution.sumBase(34, 6))
