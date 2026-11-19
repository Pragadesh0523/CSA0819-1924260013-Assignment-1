import math

fat = 4.2
snf = 8.5

# Number of fat and SNF steps
fat_steps = round((fat - 3.5) / 0.1)
snf_steps = round((snf - 8.0) / 0.1)

# Example rate calculation
rate = 30 + 2 * fat_steps + 1.5 * snf_steps

# Amount calculation
litres = 10
amount = rate * litres

print("Fat steps:", fat_steps)
print("SNF steps:", snf_steps)
print("Rate per litre:", rate)
print("Total amount:", amount)