#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int maxArea(vector<int>& height) {
        int left = 0, right = height.size() - 1;
        int volume = 0;
        
        while (left != right) {
            volume = max(volume, (right - left) * min(height[left], height[right]));
            if (height[left] <= height[right])
                ++left;
            else
                --right;
        }
        
        return volume;
    }
};