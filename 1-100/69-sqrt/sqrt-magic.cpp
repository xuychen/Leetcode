class Solution {
public:
    int mySqrt(int x) {
            
        float f = (float) x;
        float a = f;
        unsigned int i = *(unsigned int *) &f;
        i = (i + 0x3f76cf62) >> 1;
        f = *(float *)&i;
        f = (f + a / f) * 0.5;
        f = (f + a / f) * 0.5;
        
        unsigned int xi = (unsigned int) f;
        
        if (xi * xi > x)
            return xi - 1;
        else if ((xi + 1) * (xi + 1) > x)
            return xi;
        else
            return xi + 1;
    }
};