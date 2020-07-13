from collections import defaultdict
from itertools import count
import heapq

class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """

        self.timestamp = count()
        self.follows = defaultdict(set)
        self.tweets = defaultdict(list)


    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: None
        """

        self.tweets[userId].append((next(self.timestamp), tweetId))


    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """

        followees = self.follows[userId]
        all_tweets = reduce(lambda a, b: a + b, map(lambda x: self.tweets[x][-10:], followees), self.tweets[userId])
        return map(lambda x: x[1], heapq.nlargest(10, all_tweets))


    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """

        if followerId == followeeId:
            return

        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """

        self.follows[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)