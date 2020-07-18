class RandomizedCollection {
public:
    vector<int> nums;
    unordered_multimap<int, int> m;

    /** Initialize your data structure here. */
    RandomizedCollection() {
    }

    /** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
    bool insert(int val) {
        nums.emplace_back(val);
        m.insert(make_pair(val, nums.size() - 1));
        return true;
    }

    /** Removes a value from the set. Returns true if the set contained the specified element. */
    bool remove(int val) {
        auto iter = m.find(val);
        if (iter == m.end())
            return false;

        int last = nums.back();
        auto range = m.equal_range(last);
        for (auto range_iter = range.first; range_iter != range.second; ++range_iter)
            if (range_iter->second == nums.size() - 1)
                range_iter->second = iter->second;

        nums[iter->second] = last;
        nums.pop_back();
        m.erase(iter);
        return true;
    }

    /** Get a random element from the set. */
    int getRandom() {
        return nums[rand() % nums.size()];
    }
};

/**
 * Your RandomizedCollection object will be instantiated and called as such:
 * RandomizedCollection* obj = new RandomizedCollection();
 * bool param_1 = obj->insert(val);
 * bool param_2 = obj->remove(val);
 * int param_3 = obj->getRandom();
 */