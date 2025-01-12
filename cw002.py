#BMI Calculation

weight=float(input("Input your body weight(kg)..."))
height=float(input("Input your body height(m)..."))

bmi=(weight/(height*height))

if (bmi>=30):
    print("Your BMI category is Obesity.")
elif (bmi<30 and bmi>=25):
    print("Your BMI category is Overweight.")
elif (bmi<25 and bmi>=18.5):
    print("Your BMI category is Healthy Weight.")
elif (bmi<18.5 and bmi>=0):
    print("Your BMI category is Underweight.")
else:
    print("Somethings Wrong. Check your input value.")