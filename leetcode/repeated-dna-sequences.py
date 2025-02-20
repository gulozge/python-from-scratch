class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        seen = set()
        result = set()
        a = 0
        for i in range(0, len(s)):
            a = i+10
            tmp = s[i:a]
            if tmp in seen:
                result.add(tmp)
            else:
                seen.add(tmp)
        result = list(result)
        return result


solution = Solution()
print(solution.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
