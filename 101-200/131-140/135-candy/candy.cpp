class Solution {
public:
    int candy(vector<int>& ratings) {
        int start = 1;
        int length = ratings.size();
        vector<int> candies = vector<int> (length);
        vector<int> stops;
        
        if (length == 0)
            return 0;

        int result = candies[0] = 1;
        
        for (int i = 1; i < length; ++i) {
            if (ratings[i] > ratings[i-1])
                candies[i] = candies[i-1] + 1;
            else if (ratings[i] < ratings[i-1])
                candies[i] = candies[i-1] - 1;
            else {
                candies[i] = 1;
                stops.push_back(i);
            }
            
            result += candies[i];
        }
        
        stops.push_back(length);
        
        for (auto it: stops) {
            result += candy_helper(candies, start, it);
            start = it + 1;
        }
        
        return result;
    }
    
    int candy_helper(vector<int> &candies, int start, int end) {
        int minimum = 1;
        bool downFlag = true;
        int result = 0;
        int count = 1;
        
        for (; start < end && candies[start-1] < candies[start]; ++start);
        
        for (int i = start; i < end; ++i, ++count) {
            if (candies[i] < candies[i-1]) {
                if (!downFlag) {
                    downFlag = true;
                    result += (1-minimum) * (count - 1);
                    count = 1;
                }
            }
            else {
                if (downFlag) {
                    downFlag = false;
                    
                    if (minimum < candies[i-1]) {
                        --count;
                        result += 1 - minimum;
                    }
                    
                    minimum = candies[i-1];
                }
            }
        }

        if (downFlag) {        
            if (minimum < candies[end-1]) {
                --count;
                result += 1 - minimum;
            }
            
            minimum = candies[end-1];
        }

        result += (1-minimum) * count;
        return result;
    }
};