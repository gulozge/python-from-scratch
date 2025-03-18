# karmaşıklığı o(n^2)
"""class Solution:
   def twoSum(self, nums: List[int], target: int) -> List[int]:
        result=list()
        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    result.append(i)
                    result.append(j)
                    return result"""
# karmaşıklığı o(n)


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
        return []


solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9))
