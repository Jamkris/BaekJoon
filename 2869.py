import math

A, B, V = map(int, input().split())

A -= B
V -= B

print(math.ceil(V/A))
