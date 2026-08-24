class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ["(", "{", "["]:
                stack.append(c)
            else:
                match c:
                    case ")":
                        if not (stack and stack.pop() == "("):
                            return False
                    case "}":
                        if not (stack and stack.pop() == "{"):
                            return False
                    case "]":
                        if not (stack and stack.pop() == "["):
                            return False
        return not stack