// solution online

class Solution {
public:
    int videoStitching(vector<vector<int>>& clips, int T, int res = 0) {
        sort(begin(clips), end(clips));
        for (auto i = 0, st = 0, end = 0; st < T; st = end, ++res) {
            while (i < clips.size() && clips[i][0] <= st) end = max(end, clips[i++][1]);
            if (st == end)
                return -1;
        }
        return res;
    }
};