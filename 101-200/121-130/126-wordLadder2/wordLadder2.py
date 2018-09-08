class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        
        if endWord not in wordList:
            return []
        
        dictionary = {}
        for word in wordList:
            for i in range(len(word)):
                key = word[:i]+"*"+word[i+1:]
                dictionary.setdefault(key, [])
                dictionary[key].append(word)
                
        frontQueue, backQueue = [beginWord], [endWord]
        checkPoint = {beginWord: [[beginWord]], endWord: [[endWord]]}
        times = 1
        result = []
        
        # print dictionary
        while frontQueue or backQueue:
            times += 1
            newQueue = []
            for word in frontQueue:
                for i in range(len(word)):
                    for elem in dictionary.get(word[:i]+"*"+word[i+1:], []):
                        paths = checkPoint.setdefault(elem, [])
                        if paths and paths[0][0] != beginWord:
                            for prefix in checkPoint[word]:
                                for path in paths:
                                    result.append(prefix + path[::-1])             
                        elif paths == [] or len(paths[0]) == times:
                            if paths == []:
                                newQueue.append(elem)
                            for prefix in checkPoint[word]:
                                checkPoint[elem].append(prefix + [elem])
                            
            frontQueue = newQueue
            if result:
                return result
            
            newQueue = []
            for word in backQueue:
                for i in range(len(word)):
                    for elem in dictionary.get(word[:i]+"*"+word[i+1:], []):
                        paths = checkPoint.setdefault(elem, [])
                        if paths and paths[0][0] != endWord:
                            for suffix in checkPoint[word]:
                                for path in paths:
                                    result.append(path + suffix[::-1])
                        elif paths == [] or len(paths[0]) == times: 
                            if paths == []:
                                newQueue.append(elem)
                            for suffix in checkPoint[word]:
                                checkPoint[elem].append(suffix + [elem])
                                
            backQueue = newQueue
            if result:
                return result
        return []