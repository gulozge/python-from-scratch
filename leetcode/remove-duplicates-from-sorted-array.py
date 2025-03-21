class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0
        index = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[index] = nums[i]
                index = index+1
        return index


solution = Solution()
print(solution.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
