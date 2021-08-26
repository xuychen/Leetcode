class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """

        sorted_people = sorted(people)
        result = 0
        start, end = 0, len(sorted_people) - 1

        while start <= end:
            if sorted_people[start] + sorted_people[end] <= limit:
                start += 1

            end -= 1
            result += 1

        return result