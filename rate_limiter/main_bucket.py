
import time

class FakeClock:
    def __init__(self):
        self.t = 0
    def __call__(self):
        return self.t

class RateLimiter:
    def __init__(self, capacity, refill_rate, clock=time.monotonic):
        self.users = {}
        self.clock = clock

    def allow(self, user_id):
        print("ok");
        if user_id not in self.users:
            self.users[user_id] = {
                "refill_rate": self.refill_rate,
                "capacity": self.capacity,
            }
        return True


if __name__ == "__main__":
    clock = FakeClock
    limiter = RateLimiter(capacity=5, refill_rate=1, clock=clock)
    clock.t = 0

    limiter.allow("user1")