x = int(input())

for i in range(x):
  sum = 0
  a, b = map(int, input().split(' '))
  for j in range(b - a + 1):
    print()
    for k in range((b - a + 1) - j):
      sum = sum + 1
      print(sum)

  print(sum)
