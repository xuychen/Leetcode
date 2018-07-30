// KMP solution in C

void calcNext(char* str, int *next) {
    int k = -1;
    next[0] = -1;
    
    for (int i = 1; i < strlen(str); i++) {
        while (k > -1 && str[k+1] != str[i]) // going back
            k = next[k];
        
        if (str[k+1] == str[i])
            k++;
        
        next[i] = k;
    }
}

int strStr(char* haystack, char* needle) {
    int length = strlen(haystack);
    int patLength = strlen(needle);
    int *next = malloc(sizeof(int) * patLength);
    int k = -1;
    
    if (length < patLength)
        return -1;
    
    calcNext(needle, next);
    
    for (int i = 0; i < length; i++) {
        while (k > -1 && needle[k+1] != haystack[i])
            k = next[k];
        
        if (needle[k+1] == haystack[i])
            k++;
        
        if (patLength && k == patLength - 1)
            return i - patLength + 1;
    }
    
    return patLength == 0 ? 0 : -1;
}

