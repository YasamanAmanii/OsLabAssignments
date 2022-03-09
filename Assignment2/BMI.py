w = float(input("enter weight"))
h = float(input("enter height"))

BMI = w/(h*h)
print ("BMI : " , BMI)

if BMI < 18.5 :
    print("Underweight")
elif BMI <24.9 :
    print("Normal")
elif BMI <29.9 :
    print("Overweight")
elif BMI <34.5 :
    print("Obese")
else :
    print("Extremely Obese")



