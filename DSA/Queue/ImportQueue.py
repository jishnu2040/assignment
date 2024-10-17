import queue

q = queue.Queue()

q.put(40)
q.put(10)
q.put(20)
q.put(400)


q.get()
q.get()
while q:
    print(q.get())