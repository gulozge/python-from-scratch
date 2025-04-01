class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        s = s.split(" ")
        return len(s[-1])


solution = Solution()
print(solution.lengthOfLastWord("   fly me   to   the moon  "))
