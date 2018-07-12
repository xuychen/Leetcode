class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
               
        for i in range(len(gas)):
            gas[i] -= cost[i]
        
        length = len(gas)
        index = length - 1
        result = gas[0]
        for i in range(length-1):
            next = i + 1
            result += gas[next]
            sum = gas[i] + gas[next]
            if (sum >= 0 and gas[i] >= 0) or gas[i] * gas[next] > 0:
                gas[next] = sum
                if index == length - 1:
                    index = i
            else:
                index = length - 1
            
        if result < 0:
            return -1
        else:       
            return index 