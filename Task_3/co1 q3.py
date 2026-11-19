# Named constants
BASE_RATE = 30.0
FAT_RATE = 0.40
SNI_RATE = 0.30

# Input
base = float(input("Enter base amount: "))
category = input("Enter category (fat/sni): ").lower()

# Calculate rate
if category == "fat":
    rate = FAT_RATE
elif category == "sni":
    rate = SNI_RATE
else:
    rate = BASE_RATE

total = base * rate

print("Rate:", rate)
print("Total amount:", total)