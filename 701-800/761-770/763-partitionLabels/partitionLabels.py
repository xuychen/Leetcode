class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """

        dictionary = {}
        index = -1
        counter = []

        for char in S:
            if char not in dictionary:
                index += 1
                dictionary[char] = index
                counter.append(0)
            elif dictionary[char] != index:
                for key in dictionary:
                    dictionary[key] = min(dictionary[key], dictionary[char])

                for _ in range(index-dictionary[char]):
                    counter[dictionary[char]] += counter.pop()

                index = dictionary[char]

            counter[index] += 1

        return counter

    def partition_labels(self, S):
        rightmost = {c:i for i, c in enumerate(S)}
        left, right = 0, 0

        result = []
        for i, letter in enumerate(S):

            right = max(right,rightmost[letter])

            if i == right:
                result += [right-left + 1]
                left = i+1

        return result