
list=[]

n=int(input())

for x in range(n):
    m=int(input("Input a number..."))
    list.append(m)
sum=0.0
for f in list:
    if f%2!=0:
        sum=sum+f
print(sum)