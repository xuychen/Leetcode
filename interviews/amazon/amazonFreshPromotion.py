def promotion(codeList, shoppingCart):
    start = 0
    cartLen = len(shoppingCart)
    for code in codeList:
        i, end = 0, start
        length = len(code)
        
        while i < length and start < cartLen:
            item = code[i]
            if item == "anything" or item == shoppingCart[end]:
                end += 1
                i += 1
            else:
                start += 1
                end = start
                i = 0

        if i == length:
            start = end
        elif start == cartLen:
            return False

    return True

codeList1 = [ [ "apple", "apple" ], [ "banana", "anything", "banana" ] ]
shoppingCart1 = ["orange", "apple", "apple", "banana", "orange", "banana"]
codeList2 = [ [ "apple", "apple" ], [ "banana", "anything", "banana" ] ]
shoppingCart2 = ["banana", "orange", "banana", "apple", "apple"]
codeList3 = [ [ "apple", "apple" ], [ "banana", "anything", "banana" ] ]
shoppingCart3 = ["apple", "banana", "apple", "banana", "orange", "banana"]
codeList4 = [ [ "apple", "apple" ], [ "apple", "apple", "banana" ] ]
shoppingCart4 = ["apple", "apple", "apple", "banana"]
codeList5 = [ [ "apple", "apple" ], [ "banana", "anything", "banana" ] ]
shoppingCart5 = ["orange", "apple", "apple", "banana", "orange", "banana"]
codeList6 = [ [ "apple", "apple" ], [ "banana", "anything", "banana" ]  ]
shoppingCart6 = ["apple", "apple", "orange", "orange", "banana", "apple", "banana", "banana"]
codeList7= [ [ "anything", "apple" ], [ "banana", "anything", "banana" ]  ]
shoppingCart7 = ["orange", "grapes", "apple", "orange", "orange", "banana", "apple", "banana", "banana"]
codeList8 = [["apple", "orange"], ["orange", "banana", "orange"]]
shoppingCart8 = ["apple", "orange", "banana", "orange", "orange", "banana", "orange", "grape"]
codeList9= [ [ "anything", "anything", "anything", "apple" ], [ "banana", "anything", "banana" ]  ]
shoppingCart9 = ["orange", "apple", "banana", "orange", "apple", "orange", "orange", "banana", "apple", "banana"]

print(promotion(codeList1, shoppingCart1)) # True
print(promotion(codeList2, shoppingCart2)) # False
print(promotion(codeList3, shoppingCart3)) # False
print(promotion(codeList4, shoppingCart4)) # False
print(promotion(codeList5, shoppingCart5)) # True
print(promotion(codeList6, shoppingCart6)) # True
print(promotion(codeList7, shoppingCart7)) # True
print(promotion(codeList8, shoppingCart8)) # True
print(promotion(codeList9, shoppingCart9)) # True