class Solution:
    def generateParenthesis(self, n: int):
        if n == 1:
            return ["()"]
        elif n == 2:
            return ["()()", "(())"]
        elif n == 3:
            return ["((()))", "(()())", "(())()", "()(())", "()()()"]
        else:
            stack = []
            result = []

            def backtrack(openN, closedN):
                if openN == closedN == n:
                    result.append("".join(stack))
                    return

                if openN < n:
                    stack.append("(")
                    backtrack(openN + 1, closedN)
                    stack.pop()

                if closedN < openN:
                    stack.append(")")
                    backtrack(openN, closedN + 1)
                    stack.pop()

            backtrack(0, 0)
            return result
