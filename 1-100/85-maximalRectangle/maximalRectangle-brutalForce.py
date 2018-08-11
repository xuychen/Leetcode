class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        
        rows = len(matrix)
        if rows == 0:
            return 0
        cols = len(matrix[0])
        maxRect = 0
        
        # (x, y), x is rows, y is cols
        storage = [[(1,1) for i in range(cols)] for j in range(rows)]
        
        for i in range(rows):
            for j in range(cols):
                # check if 0
                if matrix[i][j] == "0":
                    continue
                    
                # get prev
                x = y = a = b = 0
                if i != 0:
                    (x, y) = storage[i-1][j]
                    x -= 1
                if j != 0:
                    (a, b) = storage[i][j-1]
                    b -= 1
                if x * y < a * b:
                    x = a
                    y = b
                
                # expand
                rowStart = i + x
                colStart = j + y
                rowEnd = rows
                colEnd = cols
                
                if i == 5 and j == 1:
                    print x, y
                    
                # expand cols first
                for rowRange in range(i, rowStart):
                    colRange = colStart
                    while True:
                        if colRange == colEnd or matrix[rowRange][colRange] == "0":
                            colEnd = colRange
                            if (colEnd - j) * (rowRange - i + 1) > x * y:
                                x = rowRange - i + 1
                                y = colEnd - j
                            break
                        
                        colRange += 1
                        
                if i == 5 and j == 1:
                    print x, y
                # expand rows
                for rowRange in range(rowStart, rowEnd):
                    colRange = j
                    while True:
                        if colRange == colEnd or matrix[rowRange][colRange] == "0":
                            colEnd = colRange
                            if i == 5 and j == 1:
                                print x, y
                            if (colEnd - j) * (rowRange - i + 1) > x * y:
                                x = rowRange - i + 1
                                y = colEnd - j
                            break
                        colRange += 1
                
                storage[i][j] = (x, y)
                # print i, j, storage[i][j]
                if maxRect < x * y:
                    maxRect = x * y
        
        return maxRect