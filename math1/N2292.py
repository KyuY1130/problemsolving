#1:1, 2:6(2*6-6), 3:12(3*6-6), 4:18(4*6-6):
#1:1, 2:7(1+6),3:19(1+6+12),4:37(1+6+12+18),5:61(1+6+12+18+24)
N=int(input())
sum=1
i=1
while sum<N:
  sum+=6*i
  i+=1
print(i)
