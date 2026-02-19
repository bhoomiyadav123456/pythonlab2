age = int(input("Enter age: "))
heart_rate = input("Is heart rate abnormal? (yes/no): ")
severe_injury = input("Severe injury? (yes/no): ")

if heart_rate == "yes" or severe_injury == "yes":
    category = "Critical"
else:
    category = "Moderate"

if age > 65 and category == "Moderate":
    category = "Critical"

print("Patient Category: - hospitalemergency.py:13", category)
