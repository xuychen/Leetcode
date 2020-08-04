class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """

        chars.append('end')
        prev = chars[0]
        counter = 1
        index = count(1)

        for i in range(1, len(chars)):
            if chars[i] != prev:
                if counter > 1:
                    for digit in str(counter):
                        chars[next(index)] = digit

                counter = 1
                chars[next(index)] = prev = chars[i]
            else:
                counter += 1

        return next(index) - 1