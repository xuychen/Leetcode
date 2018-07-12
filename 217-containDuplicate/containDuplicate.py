class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        dictionary = {}
        for elem in nums:
            if dictionary.get(elem, False) == True:
                return True
            dictionary[elem] = True
        
        return False