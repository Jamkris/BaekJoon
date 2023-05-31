a,b = map(int, input().split())
li1=list(map(int,str(a)))
li2=list(map(int,str(b)))
num=0

for i in range(len(li1)):
  for j in range(len(li2)):
    num += li1[i]*li2[j]

    
print(num)
