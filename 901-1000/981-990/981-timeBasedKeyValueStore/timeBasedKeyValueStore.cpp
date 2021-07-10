#include <unordered_map>
#include <map>
#include <string>

using namespace std;

class TimeMap {
public:
    /** Initialize your data structure here. */
    unordered_map<string, map<int, string>> timeMap;

    TimeMap() {
    }

    void set(string key, string value, int timestamp) {
        timeMap[key][timestamp] = value;
    }

    string get(string key, int timestamp) {
        if (timeMap[key].size() > 0) {
            auto iter = timeMap[key].upper_bound(timestamp);
            if (iter == timeMap[key].end())
                return timeMap[key].rbegin()->second;
            else if (iter == timeMap[key].begin())
                return "";
            else
                return (--iter)->second;
        }

        return "";
    }
};

/**
 * Your TimeMap object will be instantiated and called as such:
 * TimeMap* obj = new TimeMap();
 * obj->set(key,value,timestamp);
 * string param_2 = obj->get(key,timestamp);
 */