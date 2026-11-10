class Twitter:

    def __init__(self):
        self.time = 0
        # userId -> list of (time, tweetId)
        # 每位使用者只儲存自己發過的推文
        self.user_tweets = defaultdict(list)
        # userId -> set of followeeIds
        # 紀錄使用者追蹤了哪些人
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        # 只記錄在該發文者自己的清單中
        self.user_tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        max_heap = []

        # 包含自己追蹤的人 + 使用者自己
        users = self.following[userId] | {userId}

        # 1. 收集每個目標使用者「最新的一則推文」放入 Heap 中
        for u in users:
            tweets = self.user_tweets[u]
            if tweets:
                last_idx = len(tweets) - 1
                t_time, t_id = tweets[last_idx]
                # Python 預設為 Min-Heap，將 time 轉負數以實現 Max-Heap
                # 儲存結構: (-time, tweetId, userId, index_in_user_tweets)
                max_heap.append((-t_time, t_id, u, last_idx))

        heapq.heapify(max_heap)

        # 2. 多路歸併取前 10 則最新推文
        while max_heap and len(res) < 10:
            neg_time, t_id, u, idx = heapq.heappop(max_heap)
            res.append(t_id)

            # 若該使用者還有更早的推文，將前一則推文放入 Heap 繼續比較
            if idx > 0:
                prev_time, prev_id = self.user_tweets[u][idx - 1]
                heapq.heappush(max_heap, (-prev_time, prev_id, u, idx - 1))

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # discard 不會在 key 不存在時拋出 KeyError
        self.following[followerId].discard(followeeId)
