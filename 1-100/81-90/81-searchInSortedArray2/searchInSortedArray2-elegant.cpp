class Solution {
   public:
    bool search(int A[], int n, int target) {
        int lo = 0, hi = n - 1, mid = 0;

        while (lo < hi) {
            mid = (lo + hi) / 2;
            if (A[mid] == target) return true;
            if (A[mid] > A[hi]) {
                if (A[mid] > target && A[lo] <= target)
                    hi = mid;
                else
                    lo = mid + 1;
            } else if (A[mid] < A[hi]) {
                if (A[mid] < target && A[hi] >= target)
                    lo = mid + 1;
                else
                    hi = mid;
            } else {
                hi--;
            }
        }
        return A[lo] == target ? true : false;
    }
};