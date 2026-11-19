
from decimal import Decimal, ROUND_HALF_UP

BASE_RATE = Decimal("32.00")
FAT_STEP_RATE = Decimal("0.45")
FAT_STEP_SIZE = Decimal("0.10")

# Replace with the actual bonus announced by the union.
BONUS_PER_LITRE = Decimal("0.00")


def calculate_rate(fat, season):
    steps = int(fat / FAT_STEP_SIZE)
    rate = BASE_RATE + steps * FAT_STEP_RATE

    # Add season-specific rules here when provided.
    if season == "off":
        rate = rate

    return rate


def calculate_bonus(litres):
    if litres > 500:
        return BONUS_PER_LITRE
    return Decimal("0.00")


def calculate_payment(fat, snf, litres, season):
    rate = calculate_rate(fat, season)
    bonus = calculate_bonus(litres)

    total_rate = rate + bonus
    payment = total_rate * litres

    return rate, bonus, payment


fat = Decimal(input("Enter fat value: "))
snf = Decimal(input("Enter SNF value: "))
litres = Decimal(input("Enter litres supplied in 10 days: "))
season = input("Enter season (peak/off): ").strip().lower()

rate, bonus, payment = calculate_payment(
    fat, snf, litres, season
)

print(f"Fat: {fat:.2f}")
print(f"SNF: {snf:.2f}")
print(f"Base milk rate: Rs. {rate:.2f}")
print(f"Bonus per litre: Rs. {bonus:.2f}")
print(
    "Total payment: Rs.",
    payment.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
)
