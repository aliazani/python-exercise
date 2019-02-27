from collections import deque

d = deque([1, 2, 3, 4, 5])
d2 = deque([1, 2, 3, 4, 5, 6, 7], maxlen=8)
for i in range(1, 5):
    d.rotate(i)
    print(d)


