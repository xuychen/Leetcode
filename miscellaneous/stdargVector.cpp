#include <vector>
#include <iostream>
#include <cstdarg>

using namespace std;

template <typename T>
class Vector {
    vector<T> data;
public:
    Vector() {};
    Vector(T num1, ...);
    Vector(const vector<T>& vec);

    vector<T> _getData() const;
    void push_back(T num);
    Vector<T> operator+(const Vector<T>& rhs) const;
    Vector<T> operator-(const Vector<T>& rhs) const;
    T operator*(const Vector<T>& rhs) const;
    friend ostream& operator<<(ostream& os, const Vector<T>& vec) {
        vector<T> vecData = vec._getData();
        size_t i = 0;
        for (; i < vecData.size()-1; ++i)
            os << vecData[i] << " ";

        if (vecData.size() > 0)
            os << vecData[i] << endl;

        return os;
    }
};

template<typename T>
Vector<T>::Vector(T num1, ...) {
    va_list vaPtr;
    va_start(vaPtr, num1);
    data.push_back(num1);
    while ((num1 = va_arg(vaPtr, T)) != 0)
        data.push_back(num1);

    va_end(vaPtr);
}

template<typename T>
Vector<T>::Vector(const vector<T>& vec) {
    for (T it: vec)
        data.push_back(it);
}

template<typename T>
vector<T> Vector<T>::_getData() const {
    return data;
}

template<typename T>
void Vector<T>::push_back(T num) {
    data.push_back(num);
}

template<typename T>
Vector<T> Vector<T>::operator+(const Vector<T>& rhs) const {
    Vector<T> result;
    vector<T> rhsData = rhs._getData();
    for (size_t i = 0; i < data.size(); ++i)
        result.push_back(data[i] + rhsData[i]);

    return result;
}

template<typename T>
Vector<T> Vector<T>::operator-(const Vector<T>& rhs) const {
    Vector<T> result;
    vector<T> rhsData = rhs._getData();
    for (size_t i = 0; i < data.size(); ++i)
        result.push_back(data[i] - rhsData[i]);

    return result;
}

template<typename T>
T Vector<T>::operator*(const Vector<T>& rhs) const {
    T result = 0;
    vector<T> rhsData = rhs._getData();
    for (size_t i = 0; i < data.size(); ++i)
        result += data[i] * rhsData[i];

    return result;
}

int main() {
    vector<double> vlhs = {1.1,2.0,30.1};
    // vector<double> vrhs = {1,2.5,4};
    Vector<double> lhs = Vector<double>(vlhs);
    Vector<double> rhs = Vector<double>(3,2.0,11.1);

    cout << lhs << rhs << lhs + rhs << lhs - rhs << lhs * rhs << endl;
    return 0;
}