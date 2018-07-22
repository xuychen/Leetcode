class Solution(object):
    def lookAhead(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        
        print "in lookahead"
        print s
        print p
        sLength = len(s)
        pLength = len(p)
        i = 0
        j = 2
    
        while True:
            if j == pLength and i < sLength:
                if p[j-2] == '.':
                    return True
                elif p[j-2] == s[i]:
                    while i < sLength and p[j-2] == s[i]:
                        i += 1
                    if i == sLength:
                        return True
                    else:
                        return False
                else:
                    return False
                
            if i == sLength:
                # print "look ahead, s ends"
                return self.isMatch(s[i:], p[j:])
            if p[0] != '.' and p[0] != s[i]:
                return self.isMatch(s[i:], p[j:])
            
            if self.isMatch(s[i:], p[j:]):
                return True
            else:
                i += 1         
            
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        
        sLength = len(s)
        pLength = len(p)
          
        i = j = 0
        print "call isMatch"
        print s
        print p        
        
        while j < pLength:
            if pLength - j <= 2 or p[j+1] != "*":
                return False
            
            chr1 = s[i]
            chr2 = p[j]
            if chr2 == ".": # if it is .
                # print "first"
                i += 1
                j += 1
            elif chr2 == "*": # if it is *, invoke lookAhead
                # print "here"
                if j - 1 < 0:
                    return False
                
                prev = p[j-1]
                if prev == "*": # case that is impossible
                    return False
                else:
                    return self.lookAhead(s[i-1:], p[j-1:])    
            elif chr1 == chr2: # the same
                # print "the same"
                i += 1
                j += 1
            elif j + 1 < pLength and p[j+1] == "*": # when * means 0 fit, but prev != '.'
                # print "in 0 fit"
                j += 2
            else:
                return False
        
        print i, sLength
        print j, pLength
        # only True case is both reaching the end
        if i == sLength:
            if j == pLength:
                return True
            elif p[j] == '*': # when case is s = 'a' p = 'a*b'
                return self.lookAhead(s[i-1:], p[j-1:])
            elif pLength - j >= 2 and p[j+1] == "*": 
                return self.lookAhead(s[i:], p[j:])
            else:
                return False
        else:
            return False