class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """

        count = maxWidth
        start = end = 0
        result = []

        for word in words:
            length = len(word)
            nSpaces = end - start - 1

            if length + nSpaces + 1 > count:
                average = count / (nSpaces or 1)
                remainder = count - average * (nSpaces or 1)
                string = words[start] + (nSpaces == 0) * average * " "

                for index in range(start+1, end):
                    string += average * " " + (remainder > 0) * " " + words[index]
                    remainder -= 1

                start = end
                count = maxWidth
                result.append(string)

            count -= length
            end += 1

        string = words[start]
        nSpaces = end - start - 1
        for index in range(start+1, end):
            string += " " + words[index]

        result.append(string + " " * (count - nSpaces))
        return result

    def fullJustify2(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """

        memory = []
        memory_size = 0
        word_count = 0
        result = []

        for word in words:
            word_length = len(word)
            if word_count + memory_size + word_length <= maxWidth:
                memory.append(word)
                memory_size += 1
                word_count += word_length
            else:
                string = memory[0]
                if memory_size == 1:
                    string += " " * (maxWidth - word_count)
                else:
                    quotient = (maxWidth - word_count) / (memory_size - 1)
                    remainder = (maxWidth - word_count) % (memory_size - 1)

                    for i in range(memory_size-1):
                        string += " " * quotient + " " * (i < remainder)
                        string += memory[i+1]

                memory = [word]
                memory_size = 1
                word_count = word_length
                result.append(string)

        result.append(" ".join(memory) + " " * (maxWidth - word_count - memory_size + 1))
        return result
