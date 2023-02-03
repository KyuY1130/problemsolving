t= int(input())
for i in range(t):
  k=int(input())
  n=int(input())
  b=[]
  for i in range(n):
      b.append(i+1)
  for i in range(k):
    a=[]
    sum=0
    for i in b:
      sum+=i
      a.append(sum)
    b=a
  print(b[-1])
    