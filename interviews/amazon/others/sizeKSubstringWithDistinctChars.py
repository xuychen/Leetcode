from collections import Counter

def distinctSubstring(s, k):
    counter = Counter(s[:k])
    num = k - len(counter)
    result = set([s[:k]]) if not num else set()

    for i in range(k, len(s)):
        counter[s[i]] += 1
        if counter[s[i]] == 1:
            num -= 1

        counter[s[i-k]] -= 1
        if counter[s[i-k]] == 0:
            num += 1

        if not num:
            result.add(s[i-k+1: i+1])

    return list(result)

s1 = "abcabc"
k1 = 3
s2 = "abacab"
k2 = 3
s3 = "awaglknagawunagwkwagl"
k3 = 4

print(distinctSubstring(s1, k1)) # ['cab', 'abc', 'bca']
print(distinctSubstring(s2, k2)) # ['cab', 'bac']
print(distinctSubstring(s3, k3)) # ["wagl", "aglk", "glkn", "lkna", "knag", "gawu", "awun", "wuna", "unag", "nagw", "agwk", "kwag"]