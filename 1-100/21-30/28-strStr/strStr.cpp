// to get rid of compiling errors
#include <string>

// KMP solution in C++
class Solution {
   private:
    void calcNext(string& str, int* next) {
        int k = -1;
        next[0] = -1;

        for (int i = 1; i < str.size(); i++) {
            while (k > -1 && str[k + 1] != str[i]) k = next[k]; // going back
            if (str[k + 1] == str[i]) k++;
            next[i] = k;
        }
    }

   public:
    int strStr(string& haystack, string& needle) {
        int length = haystack.size();
        int patLength = needle.size();
        int* next = new int[patLength];
        int k = -1;

        calcNext(needle, next);

        for (int i = 0; i < length; i++) {
            while (k > -1 && needle[k + 1] != haystack[i]) k = next[k];
            if (needle[k + 1] == haystack[i]) k++;
            if (patLength && k == patLength - 1) return i - patLength + 1;
        }

        return patLength == 0 ? 0 : -1;
    }
};