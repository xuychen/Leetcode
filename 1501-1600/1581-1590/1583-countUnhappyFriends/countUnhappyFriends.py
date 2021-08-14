class Solution:
    def unhappyFriends(self, n, preferences, pairs):
        order = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n - 1):
                order[i][preferences[i][j]] = j

        match = [0] * n
        for x, y in pairs:
            match[x] = y
            match[y] = x

        unhappyCount = 0
        for x in range(n):
            y = match[x]
            index = order[x][y]
            for i in range(index):
                u = preferences[x][i]
                v = match[u]
                if order[u][x] < order[u][v]:
                    unhappyCount += 1
                    break

        return unhappyCount

# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/count-unhappy-friends/solution/tong-ji-bu-kai-xin-de-peng-you-by-leetcode-solutio/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。