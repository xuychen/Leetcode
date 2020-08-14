class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """

        words.sort(key=lambda x: len(x))
        pre_word = set([words[0]])
        result = []

        for i in range(1, len(words)):
            word = words[i]
            length = len(word)
            dp = [True] + [False] * length

            for j in range(1, length+1):
                for k in range(j):
                    if dp[k] and word[k:j] in pre_word:
                        dp[j] = True
                        break

            if dp[-1]:
                result.append(word)

            pre_word.add(word)


        return result