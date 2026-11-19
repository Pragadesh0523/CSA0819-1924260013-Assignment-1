
# Rate constants
PETROL_RATE = 100
DIESEL_RATE = 90

def rate_per_litre(fuel_type):
    """Return the price per litre for the given fuel type."""
    if fuel_type.lower() == "petrol":
        return PETROL_RATE
    elif fuel_type.lower() == "diesel":
        return DIESEL_RATE
    else:
        return 0


def payout(litres, rate):
    """Calculate and return the payout for the given litres and rate."""
    return litres * rate


def ten_day_total(daily_payouts):
    """Return the total payout for ten days."""
    return sum(daily_payouts)


# Main program
daily_payouts = []

for day in range(1, 11):
    fuel_type = input("Enter fuel type (petrol/diesel): ")
    litres = float(input("Enter litres: "))

    rate = rate_per_litre(fuel_type)
    amount = payout(litres, rate)

    daily_payouts.append(amount)
    print("Daily payout:", amount)

total = ten_day_total(daily_payouts)
print("Total payout for 10 days:", total)
