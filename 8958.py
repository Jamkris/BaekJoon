a=int(input()) #반복 횟수 입력
ox = [] #OX 입력값 저장

count=0 #연속된 숫자 만큼 올라가는 수
main_count=0 #연속된 숫자를 더할 변수
main=[] #main_count를 담을 리스ㅡ

#OX입력 받는 for문
for i in range(a):
	ox.append(input())

i=0
while i<a:
	for j in ox[i]: #OX리스에 저장된 값을 하나씩 꺼내옴
		if j=="O": #꺼내온 j가 O면
			count += 1 # !중요 만약 연속된 숫자가 나왔을 때를 위해 main_count변수를 만들어준거임 j가 아니라면 다시 count는 0이 되고 main은 남아있게 되는 원리
			main_count += count
			
		elif j!="O":
			count = 0

	i+=1
	main.append(main_count)
	main_count = 0
	count = 0

	
for m in range(a):
	print(main[m])
