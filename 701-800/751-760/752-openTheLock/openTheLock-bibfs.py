import Queue

class Solution(object):
    def update(self, qe, visited, visited_back, deadends_set, state_shift, step):
        while not qe.empty():
            curr, count = qe.get()
            if curr in visited_back:
                return count + visited_back[curr]
            if curr not in visited and curr not in deadends_set:
                for i in range(4):
                    for next_digit in state_shift[curr[i]]:
                        next_state = curr[:i] + next_digit + curr[i+1:]
                        qe.put((next_state, count+1))

                visited[curr] = count

            if count != step:
                break

        return -1

    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """

        if target == "0000":
            return 0

        qe = Queue.Queue(maxsize = 0)
        qe_back = Queue.Queue(maxsize = 0)
        qe.put(("0000",0))
        qe_back.put((target,0))
        state_shift = {}
        counts = 0

        for i in range(10):
            if i == 0:
                state_shift[chr(i+48)] = ("9", "1")
            elif i == 9:
                state_shift[chr(i+48)] = ("8", "0")
            else:
                state_shift[chr(i+48)] = (chr(i+47), chr(i+49))

        deadends_set = set(deadends)
        visited = {}
        visited_back = {}

        while not qe.empty() and not qe_back.empty():
            value = self.update(qe, visited, visited_back, deadends_set, state_shift, counts)
            if value >= 0:
                return value
            back_value = self.update(qe_back, visited_back, visited, deadends_set, state_shift, counts)
            if back_value >= 0:
                return back_value

            counts += 1

        return -1