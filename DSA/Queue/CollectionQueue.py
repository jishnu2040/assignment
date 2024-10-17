import collections

q = collections.deque()

q.appendleft(10)
q.appendleft(50)
q.appendleft(80)

print(q)

q.pop()

print(q)
