import Queue

class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """

        length = len(ratings)
        candys = [0] * length
        qe = Queue.Queue(maxsize=0)

        prev = float('inf')
        for i in range(length-1):
            rating = ratings[i]
            if rating <= prev and rating <= ratings[i+1]:
                candys[i] = 1
                qe.put((i-1, 2, -1))
                qe.put((i+1, 2, 1))

            prev = rating

        if ratings[-1] <= prev:
            candys[-1] = 1
            qe.put((length-2, 2, -1))

        while not qe.empty():
            index, candy, step = qe.get()
            if 0 <= index < length and ratings[index] > ratings[index-step]:
                candys[index] = candy
                qe.put((index+step, candy+1, step))

        return sum(candys)