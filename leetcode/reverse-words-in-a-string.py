class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        s.reverse()
        """tmp=""
        for i in s:
            tmp=tmp+i+" "

        return tmp.strip()"""
        return " ".join(s)  # for yazmak yerine tek satırla da yapılabilir


solution = Solution()
print(solution.reverseWords("the sky is blue"))
