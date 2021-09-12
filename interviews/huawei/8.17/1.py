def block(nums):
    sorted_nums = sorted(nums)
    intervals = []
    for interval in sorted_nums:
        if not intervals:
            intervals.append(interval)
        else:
            start, end = interval
            if intervals[-1][1] < start:
                intervals.append(interval)
            elif intervals[-1][1] >= start:
                while intervals[-1][0] >= start:
                    intervals.pop()

                if intervals[-1][1] < start:
                    intervals.append(interval)
                else:
                    intervals[-1][1] = max(end, intervals[-1][1])

    return intervals

print(block([[1,3],[2,6],[8,10],[15,18]]))
print(block([[1,4],[4,5]]))
                