from collections import defaultdict, deque
import heapq
from typing import List

class Twitter:

    def __init__(self):
        self.userTweets = defaultdict(deque) # userId -> list of [time, tweetIds]
        self.following = defaultdict(set) # userId -> set of followeeId
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.userTweets[userId].append((-self.time, tweetId))

        if len(self.userTweets[userId]) > 10:
            self.userTweets[userId].popleft()

        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        min_heap = []

        self.following[userId].add(userId)

        for followeeId in self.following[userId]:
            tweets = self.userTweets[followeeId]

            if tweets:
                index = len(tweets) - 1
                time, tweetId = tweets[index]

                heapq.heappush(
                    min_heap,
                    (time, tweetId, followeeId, index - 1)
                )

        while min_heap and len(res) < 10:
            time, tweetId, followeeId, index = heapq.heappop(min_heap)

            res.append(tweetId)

            if index >= 0:
                next_time, next_tweetId = self.userTweets[followeeId][index]

                heapq.heappush(
                    min_heap,
                    (next_time, next_tweetId, followeeId, index - 1)
                )

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)