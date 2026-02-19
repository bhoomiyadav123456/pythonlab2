rating = int(input("Performance rating (1-5): "))
experience = int(input("Years of experience: "))
attendance = float(input("Attendance percentage: "))

if rating == 5:
    increment = 15
elif rating == 4:
    increment = 10
elif rating == 3:
    increment = 5
elif rating == 2:
    increment = 2
else:
    increment = 0

if experience > 5:
    increment += 3

if attendance > 90:
    increment += 2

print("Total Increment Percentage: - salaryincrement.py:22", increment, "%")