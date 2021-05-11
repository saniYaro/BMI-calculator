#This a simple code to calculate your BMI using your weight and height

weight = float(input("Enter your weight in CM: "))
height = float(input("Enter your height in KG: "))

BMI = weight / (height/100)**2
if BMI < 18.5:
    print("print you are underweight")
elif (BMI >= 18.5) or (BMI < 25):
    print("print you are normal")
elif (BMI >= 25) or (BMI < 30):
    print("print you are overweight")
elif BMI > 30:
    print("print you are obesity")
else:
    print("You Fucked")
