n=int(input())
y=n

sum1=0
while(n>0):
  d=n%10
  sum1=sum1+d**3
  n=n//10
if(sum1==y):
  print("yes")
else:
  print("no")
