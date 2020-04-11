class Solution:
    def get_num(self, s, start):
        index = start
        while index < len(s) and s[index].isdigit():
            index += 1

        return int(s[start:index]), index

    def calculate_helper(self, s, start):
        result, sign, index = 0, 1, start
        operator = ['+', '-']

        while index < len(s):
            if s[index].isdigit():
                num, index = self.get_num(s, index)
            elif s[index] in operator:
                result += sign * num
                sign = (-1, 1)[s[index] == "+"]
                index += 1
            elif s[index] == ' ':
                index += 1
            elif s[index] == '(':
                num, index = self.calculate_helper(s, index+1)
            elif s[index] == ')':
                break

        result += sign * num
        return result, index + 1

    def calculate(self, s):
        return self.calculate_helper(s, 0)[0]

    def calculate2(self, s):
        result, num, sign, stack = 0, 0, 1, []
        operator = ['-', '+']

        for char in s:
            if char.isdigit():
                num = 10 * num + int(char)
            elif char in operator:
                result += sign * num
                num = 0
                sign = (-1, 1)[char == "+"]
            elif char == "(":
                stack.append(result)
                stack.append(sign)
                result, sign = 0, 1
            elif char == ")":
                result += sign * num
                result *= stack.pop()
                result += stack.pop()
                num = 0
        return result + num * sign
