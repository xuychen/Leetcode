# By other Leetcode author
# Lemma 1. f(k+1) <= f(k) + 1
# Prove by induction:
# f(2) = 1 <= 0 + 1 = f(1) + 1
# Assume this hold for any 1 <= k' < k,
# If k is even, f(k + 1) = min(f(k) + 1, f(k + 2) + 1) <= f(k) + 1;
# If k is odd, denote k = 2l + 1 (l >= 1), then f(k + 1) = f(2l + 2) = 1 + f(l + 1) <= 1 + 1 + f(l) = 1 + f(2l) = 1 + f(k - 1). Also, f(k + 1) = 1 + f(l + 1) = f(2l + 2) = f(k + 1) <= f(k + 1) + 1. Hence, f(k + 1) <= min(f(k - 1) + 1, f(k + 1) + 1) = f(k) <= f(k) + 1.

# Lemma 2. f(k) <= 1 + f(k + 1), k >= 1
# Prove by induction:
# f(1) = 0 <= 1 + f(2)
# Assume this hold for any 1 <= k' < k,
# If k is odd, f(k) = min(1 + f(k - 1), 1 + f(k + 1)) <= 1 + f(k + 1)
# If k is even, denote k = 2l (l >= 1), then f(k) = f(2l) = 1 + f(l)
# 1 + f(l) <= 3 + f(l) = 2 + f(2l) = 1 + (1 + f(2l))
# 1 + f(l) <= 1 + 1 + f(l + 1) <= 3 + f(l + 1) = 2 + f(2l + 2) = 1 + (1 + f(2l + 2))
# => f(k) = 1 + f(l) <= 1 + min(1 + f(2l), 1 + f(2l + 2)) = 1 + f(2l + 1) = 1 + f(k + 1).

# Proof of (*):

# If n % 4 = 3 and n != 3, denote n = 4k + 3 where k >= 1.
# f(n - 1) = f(4k + 2) = 1 + f(2k + 1) = 1 + min(f(2k) + 1, f(2k + 2) + 1) = min(f(2k) + 2, f(2k + 2) + 2)
# f(2k) + 2 = f(k) + 3 >= f(k + 1) + 2 = 1 + f(2k + 2)
# and f(2k + 2) + 2 > f(2k + 2) + 1, so f(n - 1) >= 1 + f(2k + 2) = f(4k + 4) = f(n + 1) => f(n) = min(f(n - 1) + 1, f(n + 1) + 1) = f(n + 1) + 1.

# If n = 3, it's obvious that f(3) = min(f(2) + 1, f(2) + 2) = f(2) + 1.

# If n % 4 = 1 and n > 1, denote n = 4k + 1 where k >= 1.
# f(n - 1) = f(4k) = 1 + f(2k)
# 1 + f(2k) < 2 + f(2k)
# 1 + f(2k) = 2 + f(k) <= 3 + f(k + 1) = 2 + f(2k + 2)
# => f(n - 1) = 1 + f(2k) <= min(2 + f(2k), 2 + f(2k + 2)) = 1 + min(f(2k) + 1, f(2k + 2) + 1) = 1 + f(2k + 1) = f(4k + 2) = f(n + 1)
# => f(n) = min(f(n - 1) + 1, f(n + 1) + 1) = f(n - 1) + 1.

class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """

        count = 0

        while n > 3:
            if not n % 2:
                n /= 2
            elif n % 4 == 1:
                n -= 1
            else:
                n += 1

            count += 1

        return count + n - 1