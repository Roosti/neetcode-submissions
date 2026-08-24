class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_match = {")" : "(", "}" : "{", "]" : "["}
        for c in s:
            if c in ["(", "{", "["]:
                stack.append(c)
            else:
                if not (stack and stack.pop() == bracket_match[c]):
                    return False
        return not stack