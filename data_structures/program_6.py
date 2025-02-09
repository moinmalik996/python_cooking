import heapq


class PriorityQueue:
    
    def __init__(self):
        self._queue = []
        self._index = 0
        
    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1
        
    def pop(self):
        return heapq.heappop(self._queue)[-1]



q = PriorityQueue()

q.push("Moin", 1)
q.push("Hamza", 6)
q.push("Abbas", 5)
q.push("Haider", 7)


print('---->', q.pop())
print('---->', q.pop())
print('---->', q.pop())
            
        