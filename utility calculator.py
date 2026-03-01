#Electricity Bill Calculator
meter_no = input("Enter Meter Number: ")
past_reading = float(input("Enter Past Reading: "))
present_reading = float(input("Enter Present Reading: "))
consumed_units = present_reading - past_reading
rate_per_unit = float(input("Enter Rate per Unit: "))
bill_amount = consumed_units * rate_per_unit
print("Meter Number     :", meter_no)
print("Past Reading     :", past_reading)
print("Present Reading  :", present_reading)
print("Consumed Units   :", consumed_units)
print("Rate per Unit    :", rate_per_unit)
print("Bill Amount      :", bill_amount)
#Disscount Calculators
original_price = float(input("Enter original price of one item: "))
quantity = int(input("Enter quantity: "))
discount_percent = float(input("Enter discount percentage: "))
total_price = original_price * quantity
discount_amount = (total_price * discount_percent) / 100
final_price = total_price - discount_amount
print("Original price :", original_price)
print("Quantity:", quantity)
print("Total price:", total_price)
print("Discount %:", discount_percent)
print("Discount amount:", discount_amount)
print("Final price after discount:", final_price)
print("Total saved amount:", discount_amount)