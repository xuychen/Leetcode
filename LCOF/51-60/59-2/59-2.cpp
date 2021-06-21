#include <queue>

using namespace std;

class MaxQueue {
    deque<int> dq;
    queue<int> qe;
public:
    MaxQueue() {
    }

    int max_value() {
        return dq.empty() ? -1 : dq.front();
    }

    void push_back(int value) {
        while (!dq.empty() && value > dq.back())
            dq.pop_back();

        dq.push_back(value);
        qe.push(value);
    }

    int pop_front() {
        if (qe.empty())
            return -1;

        int value = qe.front();
        qe.pop();
        if (dq.front() == value)
            dq.pop_front();

        return value;
    }
};

/**
 * Your MaxQueue object will be instantiated and called as such:
 * MaxQueue* obj = new MaxQueue();
 * int param_1 = obj->max_value();
 * obj->push_back(value);
 * int param_3 = obj->pop_front();
 */