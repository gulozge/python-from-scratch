"""class Solution:
    def isValid(self, s: str) -> bool:
        open_brackets=list(("(","{","["))
        dic={
            "(":")",
            "{":"}",
            "[":"]"
        }
        result=[]
        for i in s:
            if i in open_brackets:
                result.append(i)
            else:
                if len(result)==0:
                    return False
                else:
                    tmp=result[-1]
                    if i == dic[tmp]:
                        result.pop()
                    else:
                        return False
        if len(result)==0:
            return True
        else:
            return False"""
# daha anlaşılır daha basit bir çözüm


class Solution:
    def isValid(self, s: str) -> bool:
        dic = {"(": ")", "{": "}", "[": "]"}
        stack = []
        for char in s:
            if char in dic:
                stack.append(char)
            else:
                if not stack or dic[stack.pop()] != char:
                    return False
        return not stack


solution = Solution()
print(solution.isValid("([])"))
