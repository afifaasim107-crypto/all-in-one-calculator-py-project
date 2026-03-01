# Weight Calculator
#gram into kg
GRAM = float(input("enter gram"))
KG = GRAM/1000
print("kilogram:", KG)
# kg into gram
KG_2 = int(input("enter Kilogram"))
GRAM_2 = KG_2*1000
print("gram:", GRAM_2)
# Currency Convert
dollars = float(input("Enter dollars: "))
rate = float(input("Enter exchange rate (1 USD = ? PKR): "))
rupees = dollars * rate
print("Rupees:", rupees)