class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ["(", "{", "["]:
                stack.append(c)
            else:
                match c:
                    case ")":
                        if stack and stack.pop() == "(":
                            continue
                        else:
                            return False
                    case "}":
                        if stack and stack.pop() == "{":
                            continue
                        else:
                            return False
                    case "]":
                        if stack and stack.pop() == "[":
                            continue
                        else:
                            return False
        return not stack