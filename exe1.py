n=int(input('n='))

if(n%2==0):
    print("Even")
else:
    print("Odd")

#Customer get discount of 10% if total amount is larger than 1000
amount=float(input('Enter the purchese amount...'))

payableAmount=amount

if(amount>=1000):
    print("Payable Amount: ",amount-(payableAmount*0.10))
else:
    print("Payable Amount: ",amount)