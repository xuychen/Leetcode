class Solution {
public:
    int candy(vector<int>& ratings) {
        vector<int> candies (ratings.size(), 1);

        // from left to right
        for (int i = 1; i < ratings.size(); ++i) {
            if (ratings[i] > ratings[i-1] && candies[i] <= candies[i-1])
                candies[i] = candies[i-1] + 1;
            else if (ratings[i] < ratings[i-1] && candies[i] >= candies[i-1])
                candies[i-1] = candies[i] + 1;
        }

        // from right to left
        for (int j = ratings.size()-2; j >= 0; --j) {
            if (ratings[j] > ratings[j+1] && candies[j] <= candies[j+1])
                candies[j] = candies[j+1] + 1;
            else if (ratings[j] < ratings[j+1] && candies[j] >= candies[j+1])
                candies[j+1] = candies[j] + 1;
        }

        return accumlate(candies.begin(), candies.end(), 0);
    }
}

