def chooseWords(words, target):
    tLength = len(target)
    res = []

    for word in words:
        length = len(word)
        option = tLength - length
        if option > 1 or option < -1:
            continue
        res += compare(word, target, option)

    return res

def compare(origin, target, option):
    # add = 1, change = 0, remove = -1, exact = -2
    i = j = 0
    length, tLength = len(origin), len(target)
    while i < length:
        if j < tLength and origin[i] == target[j]:
            i += 1
            j += 1
        else:
            if option == 1:
                j += 1
                option = -2
            elif option == 0:
                i += 1
                j += 1
                option = -2
            elif option == -1:
                i += 1
                option = -2
            else:
                return []
    
    return [origin]

print (chooseWords(["apples", "aple", "apply", "appal", "ellypse"], "apple"))