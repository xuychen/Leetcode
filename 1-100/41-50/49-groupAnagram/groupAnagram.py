class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53, \
                  59,61,67,71,73,79,83,89,97,101]
        dictionary = {}
        result = []
        groups = 0
        
        for string in strs:
            key = 1
            for char in string:
                key *= primes[ord(char) - 97]
            
            index = dictionary.get(key, -1)
            if index == -1:
                dictionary[key] = groups
                result.append([])
                groups += 1
            
            result[index].append(string)
        return result