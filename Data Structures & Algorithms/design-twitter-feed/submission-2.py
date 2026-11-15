class Twitter:

    def __init__(self):
        self.tweets = []
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append((userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        for i in range(len(self.tweets) -1, -1, -1):
            tweet_user, tweetId = self.tweets[i]
            if tweet_user == userId or tweet_user in self.following[userId]:
                res.append(tweetId)
                if len(res) == 10:
                    return res

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
