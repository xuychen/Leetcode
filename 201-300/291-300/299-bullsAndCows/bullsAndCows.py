class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """

        secret_dict, guess_dict = {}, {}
        bulls, cows = 0, 0

        for i, num in enumerate(secret):
            if num == guess[i]:
                bulls += 1
            else:
                if secret_dict.get(guess[i], 0) > 0:
                    secret_dict[guess[i]] -= 1
                    cows += 1
                else:
                    guess_dict.setdefault(guess[i], 0)
                    guess_dict[guess[i]] += 1

                if guess_dict.get(num, 0) > 0:
                    guess_dict[num] -= 1
                    cows += 1
                else:
                    secret_dict.setdefault(num, 0)
                    secret_dict[num] += 1

        return "{}A{}B".format(bulls, cows)