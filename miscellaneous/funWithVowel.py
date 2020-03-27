vowels = ['a', 'e', 'i', 'o', 'u']

def is_valid(sublist):
    for vowel in vowels:
        if vowel not in  sublist:
            return False

def helper(s, sublist, index):
    if index == len(s):
        if is_valid(sublist):
            return sublist
        else:
            return []
    else:
        if len(sublist) == 0:
            if s[index] != 'a':
                return helper(s, sublist, index+1)
            else:
                return helper(s, sublist + [s[index]], index+1)
        elif sublist[-1] == s[index]:
            return helper(s, sublist + [s[index]], index+1)
#         elif sublist[-1]

# def longestVowelSubsequence(s):
