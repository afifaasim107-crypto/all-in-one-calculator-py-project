# BMI Calculator
WEIGHT = int(input("enter weight"))
HEIGHT= float(input("enter height"))
BMI = WEIGHT / (HEIGHT*HEIGHT)
print("Bmi:",BMI)
if BMI < 18.5:
  print("underweight")
elif BMI < 25:
  print("normal weight")
elif BMI < 30:
  print("overweight")
else:
  print("0bese")
# Age Calculators
BIRTH_YEAR = int(input("enter birth year") )
CURRENT_YEAR= int(input("enter current year"))
AGE = CURRENT_YEAR-BIRTH_YEAR
print("age:",AGE)
if AGE<18:
  print("Minor")
elif AGE<65:
  print("Adult")
else:
  print("Senior citizen")

