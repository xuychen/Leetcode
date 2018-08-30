import bisect
class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        targetArray, length = [], 0
        for envelope in envelopes:
            index = bisect.bisect_left(targetArray, envelope[1], 0, length)
            if index == length:
                targetArray.append(envelope[1])
                length += 1
            else:
                targetArray[index] = envelope[1]
                
        return length
    