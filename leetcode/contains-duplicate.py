class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False


solution = Solution()
print(solution.containsDuplicate([1, 2, 3, 1]))
