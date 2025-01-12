def gcd(a,b):
    while(b!=0):
        a,b=b,a%b
    return a
num1=18
num2=12 
result=gcd(num1,num2)
print(f"gcd of {num1} and {num2} is:{result}")
