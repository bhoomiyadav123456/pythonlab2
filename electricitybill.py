units = int(input("Enter units consumed: "))
senior = input("Are you a senior citizen? (yes/no): ")

if units <= 100:
    bill = units * 5
elif units <= 300:
    bill = units * 7
else:
    bill = units * 10

if senior == "yes":
    bill *= 0.9

print("Total Electricity Bill: ₹ - electricitybill.py:14", bill)
