a = int(input())
al = []
alph = []

for _ in range(a):
	al.append(input())

alph = list(set(al))
#print(alph)  #문자열 겹치는 거 제거

alph.sort()
#print(alph)  #사전순으로 정렬

alph.sort(key=len)
#print(alph)  #개수로 정렬

print(*alph,sep='\n')