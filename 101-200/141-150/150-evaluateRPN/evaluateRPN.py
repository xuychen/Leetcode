from operator import add, sub, mul, truediv

class Solution(object):
    def mydiv(self, lhs, rhs):
        return int(truediv(lhs, rhs))

    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """

        stack = []
        operators = {"+": add, "-": sub, "*": mul, "/": self.mydiv}

        for elem in tokens:
            if elem not in operators:
                stack.append(int(elem))
            else:
                second, first = stack.pop(), stack.pop()
                stack.append(operators[elem](first, second))

        return stack[-1]
