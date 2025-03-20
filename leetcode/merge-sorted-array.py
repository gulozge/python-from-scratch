class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        nums1[m:] = nums2[:n]
        nums1.sort()


solution = Solution()
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

solution.merge(nums1, m, nums2, n)
print(nums1)
