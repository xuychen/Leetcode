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