class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {"+", "-", "*", "/"}
        for t in tokens:
            if t not in operations:
                stack.append(int(t))
            else:
                b = int(stack.pop())
                a = int(stack.pop())
                match t:
                    case "+":
                        stack.append(a + b)
                    case "-":
                        stack.append(a - b)
                    case "*":
                        stack.append(a * b)
                    case "/":
                        stack.append(int(a / b))
        return stack.pop()