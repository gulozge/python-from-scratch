class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        n = len(nums1)

        if n % 2 != 0:
            k = (n//2)+(n % 2)
            return float(nums1[k-1])
        else:
            k = (n//2)
            k = nums1[k]+nums1[k-1]
            return float(k/2)


solution = Solution()
print(solution.findMedianSortedArrays([1, 2], [3, 4]))
