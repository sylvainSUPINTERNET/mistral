from collections import deque


class RateLimiter:
    
    def __init__(self, limit: int, window: int):
        self.state = {}
        self.limit = limit
        self.window = window

    def allow(self, user_id: str, timestamp: int) -> bool:
        if user_id not in self.state:
            self.state[user_id] = deque()

        if self.state[user_id] and self.state[user_id][0] <= timestamp - self.window:
            while self.state[user_id] and self.state[user_id][0] <= timestamp - self.window:
                self.state[user_id].popleft()

            self.state[user_id].append(timestamp)
            return True

        if self.state[user_id] and len(self.state[user_id]) >= self.limit:
            return False

        self.state[user_id].append(timestamp)
    

        return True

if __name__ == "__main__":
    limiter = RateLimiter(limit=5, window=10)
    r = limiter.allow("alice", 1)   # True
    r = limiter.allow("alice", 2)   # True
    r = limiter.allow("alice", 3)   # True
    r = limiter.allow("alice", 4)   # True
    r = limiter.allow("alice", 5)   # True
    r = limiter.allow("alice", 6)   # False

    print(r)
    print(limiter.state)