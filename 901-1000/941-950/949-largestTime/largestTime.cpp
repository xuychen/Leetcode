#include <vector>

using namespace std;

class Solution {
public:
    int maxTime(int num1, int num2, int threshold) {
        if (num1 > num2)
            swap(num1, num2);

        if (num1 > threshold)
            return -1;
        else if (num1 < num2 && num2 <= threshold)
            swap(num1, num2);

        return 10 * num1 + num2;
    }

    string largestTimeFromDigits(vector<int>& nums) {
        int hour = -1, minute = -1;
        for (int i = 0; i < nums.size(); ++i){
            int k = nums.size() - i - 1;
            for (int j = i + 1; j < nums.size(); ++j) {
                int l = nums.size() - j - 1;
                int min1, min2;

                if (i == 0 && j == 3) {
                    min1 = nums[1];
                    min2 = nums[2];
                }
                else if (i == 1 && j == 2) {
                    min1 = nums[0];
                    min2 = nums[3];
                }
                else {
                    min1 = nums[k];
                    min2 = nums[l];
                }

                int hour12 = maxTime(nums[i], nums[j], 2);
                if (hour12 >= 24)
                    continue;

                int min12 = maxTime(min1, min2, 5);
                if (min12 == -1)
                    continue;

                if ((hour12 == hour && min12 > minute) || hour12 > hour) {
                    hour = hour12;
                    minute = min12;
                }
            }
        }

        if (hour < 0)
            return "";

        string sHour = hour < 10 ? "0" + to_string(hour) : to_string(hour);
        string sMinute = minute < 10 ? "0" + to_string(minute) : to_string(minute);

        return sHour + ":" + sMinute;
    }
};