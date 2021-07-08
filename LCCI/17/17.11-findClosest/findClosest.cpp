class Solution {
public:
    int findClosest(vector<string>& words, string word1, string word2) {
        int n = words.size();
        int i1 = -1;
        int i2 = -1;
        int res = INT_MAX;
        for (int i = 0; i < n; ++i) {
            if (words[i] == word1)
                i1 = i;
            if (words[i] == word2)
                i2 = i;
            if (i1 >= 0 && i2 >= 0)
                res = min(res, abs(i1-i2));
        }

        return res;
    }
};