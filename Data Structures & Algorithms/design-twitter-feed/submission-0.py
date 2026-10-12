class Twitter:

    def __init__(self):
        self.follower_to_followee = {}
        self.user_tweets = {}
        self.tweets = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append((tweetId, userId))
        self.user_tweets.setdefault(userId, []).append(tweetId)

    def getNewsFeed(self, userId: int) -> List[int]:
        result = []
        for i in range(len(self.tweets) - 1, -1, -1):
            tweetId, tweet_userId = self.tweets[i]
            if (tweet_userId == userId or tweet_userId in self.follower_to_followee.get(userId, set())
            ):
                result.append(tweetId)
                if len(result) == 10:
                    break
        
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follower_to_followee.setdefault(followerId, set()).add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follower_to_followee.get(followerId, set()).discard(followeeId)
