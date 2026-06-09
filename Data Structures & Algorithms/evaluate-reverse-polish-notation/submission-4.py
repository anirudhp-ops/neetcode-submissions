class Solution:
    def evalRPN(self, tokens) -> int:
        stack = []

        for val in tokens:
            if val == "+":
                b, a = stack.pop(), stack.pop()
                stack.append(a + b)
            elif val == "-":
                b, a = stack.pop(), stack.pop()
                stack.append(a - b)
            elif val == "*":
                b, a = stack.pop(), stack.pop()
                stack.append(a * b)
            elif val == "/":
                b, a = stack.pop(), stack.pop()
                stack.append(int(a / b))
            else:
                stack.append(int(val))

        return stack[0]
 
        