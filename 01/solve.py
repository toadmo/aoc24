from collections import Counter

with open("input.txt", "r") as f:
  lines = f.readlines()

l1, l2 = [], []

for line in lines:
  t1, t2 = line.split('   ')
  l1.append(int(t1))
  l2.append(int(t2))

l1 = sorted(l1)
l2 = sorted(l2)

p1 = 0

for x, y in zip(l1, l2):
  p1 += abs(x - y)

print(p1)

counts = Counter(l2)

p2 = 0

for x in l1:
  p2 += x * counts[x]

print(p2)