class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        size = 9
        smallSize = 3
        
        # by rows
        for i in range(size):
            dictionary = {}
            for j in range(size):
                num = board[i][j]
                if num != ".":
                    if dictionary.get(num, False) == True:
                        return False
                    else:
                        dictionary[num] = True
        
        # by cols
        for j in range(size):
            dictionary = {}
            for i in range(size):
                num = board[i][j]
                if num != ".":
                    if dictionary.get(num, False) == True:
                        return False
                    else:
                        dictionary[num] = True
                
        # by grid
        for igroup in range(size/smallSize):
            for jgroup in range(size/smallSize):
                dictionary = {}
                for i in range(igroup*smallSize, (igroup+1)*smallSize):
                    for j in range(jgroup*smallSize, (jgroup+1)*smallSize):
                        num = board[i][j]
                        if num != ".":
                            if dictionary.get(num, False) == True:
                                return False
                            else:
                                dictionary[num] = True
        
        return True