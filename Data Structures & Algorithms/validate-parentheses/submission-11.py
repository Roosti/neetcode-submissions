class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_match = {")" : "(",
                         "}" : "{",
                         "]" : "["}

        for c in s: 
            if c in bracket_match:
                if stack and stack[-1] == bracket_match[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack