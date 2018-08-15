# too slow, time limit exceeds

class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        
        stonesDict = {}
        for stone in stones:
            stonesDict[stone] = []
            
        stonesDict[0].append(0)
        
        for stone in stones:
            stoneList = stonesDict[stone]
            for step in stoneList:
                for diff in range(-1, 2):
                    nextStone = stone + step + diff
                    if nextStone in stonesDict and nextStone > stone:
                        stonesDict[nextStone].append(nextStone-stone)
        
        return stonesDict[stones[-1]] != []