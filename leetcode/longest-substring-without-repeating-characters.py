class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        count = 0
        max_count = 0
        i = 0
        j = 0
        while i < len(s):
            if s[i] not in seen:
                seen.add(s[i])
                count += 1
                i = i+1
            else:
                max_count = max(max_count, count)
                count = 0
                seen.clear()
                j = j+1
                i = j
        max_count = max(max_count, count)
        return max_count


solution = Solution()
print(solution.lengthOfLongestSubstring("abcabcbb"))
