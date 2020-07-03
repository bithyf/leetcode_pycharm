# class User:
#     tweet = []
#     follow = []
#
#     def __init__(self, userid):
#         self.id = userid
#
#     def posttweet(self, tweetID):
#         self.tweet.append(tweetID)
#
#     def getNewsFeed(self):
#         if len(self.tweet) > 10:
#             return self.tweet[0:10]
#         return self.tweet
#
#     def follow(self, followeeId: int) -> None:
#         self.follow.append(followeeId)
#
#     def unfollow(self, followeeId: int) -> None:
#         self.follow.remove(followeeId)


class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tweet = dict()
        self.follower = dict()

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        if userId in self.tweet:
            self.tweet[userId].insert(0, tweetId)
        else:
            self.tweet[userId] = [tweetId]

    def getNewsFeed(self, userId: int):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        if userId in self.tweet:
            time = []
            for t in self.tweet:
                time.append([t, self.tweet[time][0], 0])

        else:
            return None

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId in self.follower:
            self.follower[followerId].append(followeeId)
        else:
            self.follower[followerId] = [followeeId]

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId in self.follow:
            if followeeId in self.follower[followerId]:
                self.follower[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
obj = Twitter()
obj.postTweet(1,tweetId=2)
param_2 = obj.getNewsFeed(userId=1)
obj.follow(followerId=1, followeeId=3)
obj.unfollow(followerId=1, followeeId=3)


