#include <vector>

using namespace std;

class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        int left = 0, right = nums.size();
        int edgeValue = INT_MIN;

        while (left < right) {
            int middle = (left + right) / 2;

            if (nums[middle] > (middle + 1 == nums.size() ? edgeValue : nums[middle+1]))
                left = middle + 1;
            else if (nums[middle] > (middle ? nums[middle-1] : edgeValue))
                right = miidle - 1;
            else
                return middle;
        }

        return -1;
    }

    int findPeakElement2(vector<int> &num)
    {
        int low = 0;
        int high = num.size()-1;

        while(low < high)
        {
            int mid1 = (low+high)/2;
            int mid2 = mid1+1;
            if(num[mid1] < num[mid2])
                low = mid2;
            else
                high = mid1;
        }
        return low;
    }
};
