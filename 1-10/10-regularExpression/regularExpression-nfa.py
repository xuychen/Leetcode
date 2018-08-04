class Solution:
    @staticmethod
    def bypass(visit, path):
        visit_list = list(visit)
        i = 0
        while i < len(visit_list):
            if (visit_list[i], "+") in path:
                new_state = path[(visit_list[i], "+")]
                if new_state not in visit:
                    visit.add(new_state)
                    visit_list.append(new_state)
            i += 1

    def isMatch(self, s, p):
        path = {}
        state = 0
        for i, ch in enumerate(p):
            if ch == "*":
                # continue with the * pattern matching
                path[(state, (p[i-1], "*"))] = state
                # bypass the * pattern matching
                path[(state, "+")] = state + 1
                state += 1
            elif (i < len(p)-1 and p[i+1] != "*") or i == len(p)-1:
                # the normal transistion
                path[(state, ch)] = state + 1
                state += 1
        final = state
        visit = {0}
        for ch in s:
            # when we do bypass, we don't pass in the signal
            self.bypass(visit, path)
            visit = {path[(state, token)] for state in visit
                     for token in [(ch, "*"), (".", "*"), ".", ch] if (state, token) in path}
        self.bypass(visit, path)
        return final in visit