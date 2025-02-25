class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        area_a = (ax1-ax2)*(ay1-ay2)
        area_b = (bx1-bx2)*(by1-by2)

        intersection_x = max(0, min(ax2, bx2)-max(ax1, bx1))
        intersection_y = max(0, min(ay2, by2)-max(ay1, by1))
        area_intersection = intersection_x*intersection_y

        return (area_a + area_b)-area_intersection


solution = Solution()
print(solution.computeArea(ax1=-3, ay1=0, ax2=3,
      ay2=4, bx1=0, by1=-1, bx2=9, by2=2))
