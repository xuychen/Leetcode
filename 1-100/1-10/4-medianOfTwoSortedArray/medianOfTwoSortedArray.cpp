#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int N1 = nums1.size(), N2 = nums2.size();
        if (N1 < N2) {
            nums1.swap(nums2);  // Make sure A2 is the shorter one.
            swap(N1, N2);
        }

        int lo = 0, hi = N2 * 2;
        while (lo <= hi) {
            int mid2 = (lo + hi) / 2;   // Try Cut 2
            int mid1 = N1 + N2 - mid2;  // Calculate Cut 1 accordingly

            double L1 = (mid1 == 0) ? INT_MIN : nums1[(mid1 - 1) / 2];  // Get L1, R1, L2, R2 respectively
            double L2 = (mid2 == 0) ? INT_MIN : nums2[(mid2 - 1) / 2];
            double R1 = (mid1 == N1 * 2) ? INT_MAX : nums1[(mid1) / 2];
            double R2 = (mid2 == N2 * 2) ? INT_MAX : nums2[(mid2) / 2];

            if (L1 > R2)
                lo = mid2 + 1;  // A1's lower half is too big; need to move C1 left (C2 right)
            else if (L2 > R1)
                hi = mid2 - 1;  // A2's lower half too big; need to move C2 left.
            else
                return (max(L1, L2) + min(R1, R2)) / 2;  // Otherwise, that's the right cut.
        }
        return -1;
    }

    double findMedianSortedArrays2(vector<int>& nums1, vector<int>& nums2) {
        size_t length1 = nums1.size(), length2 = nums2.size();

        if (length1 > length2) {
            nums1.swap(nums2);
            swap(length1, length2);
        }

        int low = 0, high = length1;
        while (low <= high) {
            int i = (low + high) / 2;
            int j = (length1 + length2 + 1) / 2 - i;

            if (i > 0 && nums1[i-1] > nums2[j])
                high = i - 1;
            else if (i < length1 && nums2[j-1] > nums1[i])
                low = i + 1;
            else {
                int l1 = i == 0 ? INT_MIN : nums1[i-1];
                int l2 = j == 0 ? INT_MIN : nums2[j-1];
                int r1 = i == length1 ? INT_MAX : nums1[i];
                int r2 = j == length2 ? INT_MAX : nums2[j];

                return (length1 + length2) & 1 ? max(l1, l2) : (max(l1, l2) + min(r1, r2)) / 2.0;
            }
        }

        return -1;
    }
};