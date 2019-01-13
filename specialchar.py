x=input()
count=0
v=0
s=0
c=0
for i in x:
  if (i.isdigit()):
    count=count+1
  elif (i.isalpha()):
    s=s+1
  elif (i==(" ")):
    c=c+1
  else:
    v=v+1

print(v)
