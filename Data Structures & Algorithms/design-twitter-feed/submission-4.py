import heapq

class Twitter:

    def __init__(self):
        
        self.count = 0
        self.tweetlist = defaultdict(list)
        self.followerlist = defaultdict(set)
        
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetlist[userId].append([self.count, tweetId])
        self.count += 1 
        

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        following = self.followerlist[userId]
        following.add(userId)
        for val in following: 
            tweets = self.tweetlist[val]
            for tweet in tweets: 
                heapq.heappush(heap, tweet)
                if len(heap) > 10: 
                    heapq.heappop(heap) 
        res = []
        
        while heap: 
            val = heapq.heappop(heap)
            res.append(val[1])
        
        return res[::-1]
            


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followerlist[followerId].add(followeeId) 
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followerlist and followeeId in self.followerlist[followerId]: 
            self.followerlist[followerId].remove(followeeId) 
