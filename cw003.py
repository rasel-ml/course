'''Take input of integer number that is divisible by
 - 5 and 10 but not by 50
 - 3 and 6 but not by 18'''

print("This program going to determine whether a integer number is divisible by 5 and 10 but not by 50 or by 3 and 6 but not by 18")

num=int(input("Input a integer number..."))

if (num%5==0 and num%10==0 and num%50!=0):
    print(num,"is divisible by 5 and 10 but not by 50.")
elif (num%3==0 and num%6==0 and num%18!=0):
    print(num,"is divisible by 3 and 6 but not by 18.")
else:
    print(num,"is not meet any criteria.")