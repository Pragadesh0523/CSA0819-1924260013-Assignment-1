text = input("Enter amount: ")

try:
    amount = float(text)
    print(f"Amount: {amount:8.2f}")

except ValueError:
    print("Invalid input! Please enter a valid number.")