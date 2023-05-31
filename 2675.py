num = int(input())

S = []
for _ in range(num):
	a,b = input().split(' ')
	S.append(a)
	S.append(b)

for i in range(1,(num*2),2):
	for j in S[i]:
		print(j*int(S[i-1]),end='')
	print('')