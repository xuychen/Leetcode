#include <vector>

using namespace std;

long countSubarrays(vector<int> numbers, int k) {
    long result = 0;
    for (int start = 0, end = 0, value = 1; end < numbers.size(); ++end) {
        value *= numbers[end];
        while (value > k && end >= start)
            value /= numbers[start++];

        result += end - start + 1;
    }

    return result;
}