a,b=map(int,input().split(" "))

if b-45<0:
	if a-1<0:
		a=23
	else:
		a=a-1
	b=(b-45)+60
	print(f'{a} {b}')
	
else:
	print(f'{a} {b-45}')