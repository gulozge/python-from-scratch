class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        # Bu zaman karmaşıklığı bakımından O(n)
        result = 0
        for num in nums:
            result ^= num
        return result
        # Bu çözüm zaman karmaşıklı açısından O(n^2)
        """
        for x in nums:
          if nums.count(x)==1:
            return x
        """


solution = Solution()
liste = [1, 2, 1, 2, 3]
print(solution.singleNumber(liste))
