class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        nums.sort()
        nums = set(list(filter((lambda x: x > 0), nums)))

        i = 1
        while i in nums:
            i = i+1
        else:
            return i


solution = Solution()
print(solution.firstMissingPositive([7, 8, 9, 11, 12]))
