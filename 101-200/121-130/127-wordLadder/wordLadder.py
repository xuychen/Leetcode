class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        
        if endWord not in wordList:
            return 0
        
        dictionary = {}
        for word in wordList:
            for i in range(len(word)):
                key = word[:i]+"*"+word[i+1:]
                dictionary.setdefault(key, [])
                dictionary[key].append(word)
                
        frontQueue, backQueue = [beginWord], [endWord]
        times = 1
        checkPoint = {beginWord: 1, endWord: -1}
        
        while frontQueue or backQueue:
            times += 1
            frontQueue, result = self.update(frontQueue, times, dictionary, checkPoint)
            if result > 0:
                return result
            backQueue, result = self.update(backQueue, -times, dictionary, checkPoint)
            if result > 0:
                return result
        return 0
    
    def update(self, queue, times, dictionary, checkPoint):
        newQueue, result = [], 0
        for word in queue:
            for i in range(len(word)):
                key = word[:i]+"*"+word[i+1:]
                nextlist = dictionary.get(key, [])
                for elem in nextlist:
                    value = checkPoint.setdefault(elem, times)
                    if value * times < 0:
                        result = abs(times - value) - 1
                    elif value == times:
                        newQueue.append(elem)
                        
        return newQueue, result