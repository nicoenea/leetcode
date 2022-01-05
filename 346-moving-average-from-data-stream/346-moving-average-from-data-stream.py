class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.queue = []
        
        self.count = 0
        self.wSum = 0
        
    def next(self, val: int) -> float:
        tail = 0
        self.count += 1
        self.queue.append(val)
        
        if self.count > self.size:
            tail = self.queue.pop(0)
        # tail = self.queue.pop(0) if self.count > self.size 

        self.wSum = self.wSum - tail + val
        
        return self.wSum / len(self.queue)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)