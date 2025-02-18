class Solution:
    # Bu çözümün karmaşıklığı O(log n)

    """def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1:
            return True
        while n > 1:
            if n % 2 != 0:
                return False
            else:
                n = n//2
        return True"""
    # bit manipülasyonu ile çözmek hem  bellek hem de karmaşıklık açısından daha verimli karmaşıklığı-->O(1)

    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0


solution = Solution()
print(solution.isPowerOfTwo(81))
