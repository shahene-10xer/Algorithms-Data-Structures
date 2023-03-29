class MovingAverage:

    def __init__(self, size: int):
        self.queue = collections.deque()
        self.max_size = size
        self.total = 0.0

    def next(self, val: int) -> float:
        self.queue.append(val)
        length = len(self.queue)
        self.total += val
        while length > self.max_size:
            self.total -= self.queue.popleft()
            length = len(self.queue)
        return self.total / length
        
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)