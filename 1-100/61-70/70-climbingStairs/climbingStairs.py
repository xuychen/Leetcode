class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n < 3:
            return n
    
        one_step_before, two_steps_before = 2, 1
        all_ways = 0
    
        for i in range(3, n+1):
            all_ways = one_step_before + two_steps_before
            two_steps_before = one_step_before
            one_step_before = all_ways
            
        return all_ways