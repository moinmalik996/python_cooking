"""
Keeping the Last N Items:

    You want to keep a limited history of the last few items seen during iteration or during
    some other kind of processing.
"""

from collections import deque


q = deque(maxlen=3)

q.append(3)
q.append(4)
q.append(5)


print(q)

q.append(6)

print(q)


new_que = deque() # if max_length not provided then 
                  # we can pop and add elements from
                  # either side.
                  
new_que.append(1)
new_que.append(2)
new_que.append(3)
new_que.append(4)

print((new_que))

new_que.appendleft(0)

print((new_que))

new_que.popleft()

print(new_que)



