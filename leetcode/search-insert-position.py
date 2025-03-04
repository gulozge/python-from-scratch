class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        for i in range(len(nums)):
            if target == nums[i]:
                return i
            else:
                if nums[i] > target:
                    return i
        else:
            return len(nums)


solution = Solution()
print(solution.searchInsert([1, 3, 5, 6], 7))
