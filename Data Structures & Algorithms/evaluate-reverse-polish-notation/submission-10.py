class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = "+-*/"

        for t in tokens:
            if not t in operations:
                stack.append(int(t))
            else:
                second = stack.pop()
                first = stack.pop()
                val = 0

                if t == "+":
                    val = first + second
                elif t == "-":
                    val = first - second
                elif t == "*":
                    val = first * second
                else:
                    val = int(first / second)

                stack.append(val)

        return stack[-1]


                


        