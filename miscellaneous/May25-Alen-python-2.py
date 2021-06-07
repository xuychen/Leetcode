def nextPermutation(nums):
    flag = False
    for i in range(len(nums)-2, -1, -1):
        if nums[i] < nums[i+1]:
            flag = True
            pivot = nums[i]
            for j in range(len(nums)-1, i, -1):
                if nums[j] > pivot:
                    nums[i] = nums[j]
                    nums[j] = pivot
                    break
    
            nums[i+1:] = nums[:i:-1]
            break
            
    if not flag:
        nums[:] = nums[::-1]

# group_b has length of 4, and group_a has length of 3
def group(group_a, group_b):
    length_b = len(group_b)
    index = [i for i in range(0, length_b)]
    first_index = index[:]
    result = []

    while True:
        new_group_b = list(map(lambda x: group_b[x], index))
        result.append(list(zip(group_a, new_group_b)))
        nextPermutation(index)
        if index == first_index:
            break    

    return result

print(group(['a', 'b', 'c'], ['w','x','y','z']))
