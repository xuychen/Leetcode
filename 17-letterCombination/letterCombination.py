ASCII0 = 48

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
        if len(digits) == 0:
            return []
        
        dict = {2: "abc", 3: "def", 4:"ghi", 5:"jkl",
               6:"mno", 7:"pqrs", 8:"tuv", 9:"wxyz"}
        
        digit = ord(digits[0]) - ASCII0
        result = list(dict[digit])
        
        for i in range(1, len(digits)):
            digit = ord(digits[i]) - ASCII0
            string = dict[digit]
            length = len(string)
            lengthOfResult = len(result)
            result = result * length
            for j in range(length):
                for k in range(j*lengthOfResult, lengthOfResult*(j+1)):
                    result[k] += string[j]
                    
        return result