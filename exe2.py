mark=float(input("Input your number..."))

if(mark>=80 and mark<=100):
    print("You got A+")
elif(mark>=70 and mark<80):
    print("You got A")
elif(mark>=60 and mark<70):
    print("You got A-")
elif(mark>=50 and mark<60):
    print("You got B")
elif(mark>=40 and mark<50):
    print("You got C")
elif(mark>=33 and mark<40):
    print("You got D")
elif(mark>=0 and mark<33):
    print("You Failed")
else:
    print("Mark should be 0-100")
