while True:
	try: #언제까지 입력받을 지 모르기 때문에 try 함수를 사용해 용량만큼 한 뒤 except로 넘어감
		a,b=map(int,input().split(' '))
		print(a+b)
		
	except:
		break
