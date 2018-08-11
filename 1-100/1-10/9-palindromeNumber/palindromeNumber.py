class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        if x < 0:
            return False
        else:
            string = str(x)
            reverse = string[::-1]
            if string == reverse:
                return True
            else:
                return False