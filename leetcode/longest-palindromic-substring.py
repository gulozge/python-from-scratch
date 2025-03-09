class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_palindromic_substring = ""
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                tmp = s[i:j]
                if tmp == tmp[::-1]:
                    if len(tmp) > len(longest_palindromic_substring):
                        longest_palindromic_substring = tmp
        return longest_palindromic_substring


solution = Solution()
print(solution.longestPalindrome("ababaa"))
