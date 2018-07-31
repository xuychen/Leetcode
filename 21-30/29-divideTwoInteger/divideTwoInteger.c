#include <limits.h>

int divide(int dividend, int divisor) {
    long quotient = (long) dividend / divisor;
    return quotient > INT_MAX ? INT_MAX: quotient;
}