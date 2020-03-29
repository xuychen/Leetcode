#include <vector>
#include <set>

using namespace std;

class MedianHeap {
    multiset<int> minSet;
    multiset<int> maxSet;
    int _size;
public:
    MedianHeap(): _size(0) {};
    void insert(int num);
    void remove(int num);
    double getMedian();
};

void MedianHeap::insert(int num) {
    if (_size & 1) {
        if (num >= *maxSet.rbegin())
            minSet.insert(num);
        else {
            minSet.insert(*maxSet.rbegin());
            maxSet.erase((++maxSet.rbegin()).base());
            maxSet.insert(num);
        }
    }
    else {
        if (!_size || num <= *minSet.begin())
            maxSet.insert(num);
        else {
            maxSet.insert(*minSet.begin());
            minSet.erase(minSet.begin());
            minSet.insert(num);
        }
    }

    ++_size;
}

void MedianHeap::remove(int num) {
    // cout << *(++maxSet.rbegin()).base() << " " << *minSet.begin() << num << endl;
    if (_size & 1) {
        if (num <= *maxSet.rbegin())
            maxSet.erase(maxSet.find(num));
        else {
            minSet.erase(minSet.find(num));
            minSet.insert(*maxSet.rbegin());
            maxSet.erase((++maxSet.rbegin()).base());
        }
    }
    else {
        if (!_size || num >= *minSet.begin())
            minSet.erase(minSet.find(num));
        else {
            maxSet.erase(maxSet.find(num));
            maxSet.insert(*minSet.begin());
            minSet.erase(minSet.begin());
        }
    }

    --_size;
}

double MedianHeap::getMedian() {
    return _size & 1 ? *maxSet.rbegin() : ((long) *maxSet.rbegin() + *minSet.begin()) / 2.0;
}

class Solution {
public:
    vector<double> medianSlidingWindow(vector<int>& nums, int k) {
        MedianHeap mHeap;
        vector<double> result;
        int i = 0;

        for (; i < k; ++i)
            mHeap.insert(nums[i]);

        result.push_back(mHeap.getMedian());

        for (; i < nums.size(); ++i) {
            mHeap.remove(nums[i-k]);
            mHeap.insert(nums[i]);
            result.push_back(mHeap.getMedian());
        }

        return result;
    }

    vector<double> medianSlidingWindow(vector<int>& nums, int k) {
        multiset<int> window(nums.begin(), nums.begin() + k);
        auto mid = next(window.begin(), k / 2);
        vector<double> medians;
        for (int i=k; i < nums.size() ; i++) {
            // Push the current median.
            medians.push_back((double(*mid) + *prev(mid, 1 - k%2)) / 2);

            // Insert nums[i].
            window.insert(nums[i]);
            if (nums[i] < *mid)
                mid--;

            // Erase nums[i-k].
            if (nums[i-k] <= *mid)
                mid++;
            window.erase(window.lower_bound(nums[i-k]));
        }

        return medians;
    }
};