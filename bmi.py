height = int(input("Enter height: "))
weight = int(input("Enter weight: "))
bmi = weight/(height*height)
if bmi < 18.5 :
    print("Underweight")
elif bmi >= 18.5 and bmi < 24.9 :
    print("Normal")
elif bmi >=25 and bmi < 30 :
    print("Overweight")
else :
    print("Obese")
