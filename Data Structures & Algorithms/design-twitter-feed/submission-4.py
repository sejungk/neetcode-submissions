class Twitter:

    def __init__(self):
        self.userTweets = defaultdict(deque)
        self.following = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.userTweets[userId].append((-self.time, tweetId))
        if len(self.userTweets[userId]) > 10:
            self.userTweets[userId].popleft()
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        min_heap = []
        
        for user in self.following[userId] | {userId}:
            for item in self.userTweets[user]:
                heapq.heappush(min_heap, item)
        
        res = []
        while min_heap:
            time, tweetId = heapq.heappop(min_heap)
            res.append(tweetId)
            if len(res) == 10:
                return res
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
