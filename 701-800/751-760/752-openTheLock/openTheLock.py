import Queue

class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """

        if target == "0000":
            return 0

        qe = Queue.Queue(maxsize = 0)
        qe.put(("0000", 0))
        state_shift = {}

        for i in range(10):
            if i == 0:
                state_shift[chr(i+48)] = ("9", "1")
            elif i == 9:
                state_shift[chr(i+48)] = ("8", "0")
            else:
                state_shift[chr(i+48)] = (chr(i+47), chr(i+49))

        visited = set(deadends)

        while not qe.empty():
            curr, count = qe.get()
            if curr not in visited:
                for i in range(4):
                    for next_digit in state_shift[curr[i]]:
                        next_state = curr[:i] + next_digit + curr[i+1:]
                        if next_state == target:
                            return count + 1

                        qe.put((next_state, count+1))

                visited.add(curr)

        return -1