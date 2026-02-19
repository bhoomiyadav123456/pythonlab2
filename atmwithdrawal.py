balance = float(input("Enter account balance: "))
withdraw_amount = float(input("Enter withdrawal amount: "))
atm_cash = float(input("Enter ATM available cash: "))
daily_limit = 50000

if withdraw_amount > daily_limit:
    print("Error: Exceeds daily withdrawal limit (₹50,000). - atmwithdrawal.py:7")

elif withdraw_amount > balance:
    print("Error: Insufficient account balance. - atmwithdrawal.py:10")

elif withdraw_amount > atm_cash:
    print("Error: ATM does not have sufficient cash. - atmwithdrawal.py:13")

else:
    balance -= withdraw_amount
    atm_cash -= withdraw_amount
    print("Withdrawal Successful! - atmwithdrawal.py:18")
    print("Remaining Balance: ₹ - atmwithdrawal.py:19", balance)
