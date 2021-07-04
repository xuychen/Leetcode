from collections import Counter

class Solution(object):
    def counterMultiplication(self, counter, constant):
        for key in counter.keys():
            counter[key] *= constant

    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """

        formula += "#"
        stack = []
        counter = Counter()
        flag = False
        element = ""
        num = 0

        for char in formula:
            if char.islower():
                element += char
            elif char.isdigit():
                num *= 10
                num += int(char)
            else:
                if flag:
                    self.counterMultiplication(counter, num if num else 1)
                    counter += stack.pop()
                    flag = False
                else:
                    if len(element) > 0:
                        counter[element] += num if num else 1

                element = ""
                num = 0

                if char.isupper():
                    element += char
                elif char == '(':
                    stack.append(counter)
                    counter = Counter()
                elif char == ')':
                    flag = True

        return reduce(lambda x, y: x+y, map(lambda x: x + str(counter[x]) if counter[x] > 1 else x, sorted(counter.keys())), "")