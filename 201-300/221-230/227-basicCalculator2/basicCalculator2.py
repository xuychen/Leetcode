class Solution:
    def calculate(self, s):
        s += '-'
        result, num, sign, stack = 0, 0, '+', []
        operator1, operator2 = ('+', '-'), ('*', '/')

        for char in s:
            if char.isdigit():
                num = 10 * num + int(char)
            elif char in operator1:
                if sign in operator1:
                    result += (1 if sign == '+' else -1) * num
                else:
                    if sign == '*':
                        result *= num
                    else:
                        result //= num

                    result *= 1 if stack.pop() == '+' else -1
                    result += stack.pop()

                sign, num = char, 0
            elif char in operator2:
                if sign in operator1:
                    stack.append(result)
                    stack.append(sign)
                    result = num
                elif sign in operator2:
                    if sign == '*':
                        result *= num
                    else:
                        result //= num

                sign, num = char, 0

        return result