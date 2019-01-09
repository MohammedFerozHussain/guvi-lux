y=int(input())
e=y
sum=0
while(y>0):
	x=y%10
	sum=sum*10+x
	y=y//10
print(sum)
if e == sum:
  print("yes")
else:
  print("no")

