w=int(input())
li=[]
s=0
y=1
for i in range(0,w):
  temp=s+y
  s=y
  y=temp
  li.append(s)
print(*li)
