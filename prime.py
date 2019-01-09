n=int(input())
for i in range(2,n):
  h = n % i
  if h==0:
    print("no")
    break
else:
  print("yes")
    
