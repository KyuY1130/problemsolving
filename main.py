M=int(input())
N=int(input())
sosu=[]
for i in range(M,N+1):
  error=0
  if i>1:
    for s in range(2,i):
      if i%s==0:
        error+=1
    if error == 0:
      sosu.append(i)
sum=0      
for  i in sosu:
  sum+=i
print(sum)
print(min(sosu))
