#include <vector>

using namespace std;

template <typename T>
class Vector<T> {
    vector<T> data;
public:
    Vector<T>() {};
    Vector<T>(vector<T> vec);

    vector<T> getData();
    void push_back(T num);
    Vector<T> operator+(Vector<T> rhs);
    Vector<T> operator-(Vector<T> rhs);
    T operator*(Vector<T> rhs);
    friend ostream& operator<<(ostream& os, Vector<T> vec);
};

template<typename T>
Vector<T>::Vector<T>(vector<T> vec) {
    for (T it: vec)
        data.push_back(it);
}

template<typename T>
vector<T> Vector<T>::getData() {
    return data;
}

template<typename T>
void Vector<T>::push_back(T num) {
    data.push_back(num);
}

template<typename T>
Vector<T> Vector<T>::operator+(vector<T> rhs) {
    Vector<T> result;
    vector<T> rhsData = rhs.getData();
    for (size_t i = 0; i < data.size(); ++i)
        result.push_back(data[i] + rhsData[i]);

    return result;
}

template<typename T>
Vector<T> Vector<T>::operator-(vector<T> rhs) {
    Vector<T> result;
    vector<T> rhsData = rhs.getData();
    for (size_t i = 0; i < data.size(); ++i)
        result.push_back(data[i] - rhsData[i]);

    return result;
}

template<typename T>
T Vector<T>::operator*(vector<T> rhs) {
    T result = 0;
    vector<T> rhsData = rhs.getData();
    for (size_t i = 0; i < data.size(); ++i)
        result += data[i] * rhsData[i];

    return result;
}

template<typename T>
ostream& operator<<(ostream& os, vector<T> vec) {
    vector<T> vecData = vec.getData();
    size_t i = 0;
    for (; i < vecData.size()-1; ++i)
        os << vecData[i] << " ";

    if (vecData > 0)
        os << vecData[i] << endl;

    return os;
}