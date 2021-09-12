#include <iostream>

using namespace std;

int main() {
    int x, y, a, b;
    cin >> x >> y >> a >> b;

    int max1 = min(x / a, y / b);
    int max2 = 0;
    int total = max1 + max2;

    while (max1 > 0) {
        ++max2;
        max1 = min((x-b*max2) / a, (y-a*max2) / b);

        if (max1 + max2 > total)
            total = max1 + max2;
        else if (max1 + max2 < total)
            break;
    }

    cout << total << endl;
    return 0;
}

