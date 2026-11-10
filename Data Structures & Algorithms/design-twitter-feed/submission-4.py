class Twitter:

    def __init__(self):
        self.time = 0
        self.user_tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.user_tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        max_heap = []

        users = self.following[userId] | {userId}
        for u in users:
            tweets = self.user_tweets[u]
            if tweets:
                last_idx = len(tweets) - 1
                t_time, t_id = tweets[last_idx]
                max_heap.append((-t_time, t_id, u, last_idx))
        heapq.heapify(max_heap)

        while max_heap and len(res) < 10:
            neg_time, t_id, u, idx = heapq.heappop(max_heap)
            res.append(t_id)
            if idx > 0:
                prev_time, prev_id = self.user_tweets[u][idx - 1]
                heapq.heappush(max_heap, (-prev_time, prev_id, u, idx - 1))
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
