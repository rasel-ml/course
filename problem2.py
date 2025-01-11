#Student Grade Calculator

ban=float(input("Input your exam mark for Bangla..."))
eng=float(input("Input your exam mark for English..."))
math=float(input("Input your exam mark for Math..."))

avg=(ban+eng+math)/3

if(avg>=90 and avg<=100):
    print("Your Average mark:",avg,"You Result: Grade A")
elif(avg>=80 and avg<90):
    print("Your Average mark:",avg,"You Result: Grade B")
elif(avg>=70 and avg<80):
    print("Your Average mark:",avg,"You Result: Grade C")
elif(avg>=60 and avg<70):
    print("Your Average mark:",avg,"You Result: Grade D")
elif(avg>=0 and avg<60):
    print("Your Average mark:",avg,"You Result: Fail")
else:
    print("Mark should be 0-100")