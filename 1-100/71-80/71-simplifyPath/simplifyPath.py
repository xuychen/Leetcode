class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """

        stack = []
        stackPtr = stackLength = 0
        i = 1
        length = len(path)
        
        while i < length:
            word = ""
            while i < length and path[i] != "/":
                word += path[i]
                i += 1
            
            i += 1
            if word == "..":
                stackPtr = stackPtr - 1 if stackPtr else stackPtr
            elif word not in {".", ""}:
                if stackPtr == stackLength:
                    stack.append(word)
                    stackPtr = stackLength = stackLength + 1
                else:
                    stack[stackPtr] = word
                    stackPtr += 1  
    
        return "/" + "/".join(stack[:stackPtr])