
from decimal import Decimal, ROUND_HALF_UP
import time

sizes = [300, 6000, 150000]
rate = Decimal("12.345")

for n in sizes:
    quantities = [(i % 100) + 1 for i in range(n)]

    # Float calculation
    start = time.perf_counter()
    float_total = sum(q * float(rate) for q in quantities)
    float_time = time.perf_counter() - start

    # Decimal calculation
    start = time.perf_counter()
    decimal_total = sum(
        Decimal(q) * rate for q in quantities
    )
    decimal_time = time.perf_counter() - start

    # Round each payment
    rounded_payments = sum(
        (Decimal(q) * rate).quantize(
            Decimal("0.01"), rounding=ROUND_HALF_UP
        )
        for q in quantities
    )

    # Round only the final total
    rounded_total = decimal_total.quantize(
        Decimal("0.01"), rounding=ROUND_HALF_UP
    )

    print("\nPayments:", n)
    print("Float total:", round(float_total, 2))
    print("Decimal total:", decimal_total)
    print("Difference:", abs(Decimal(str(float_total)) - decimal_total))
    print("Float time:", float_time, "seconds")
    print("Decimal time:", decimal_time, "seconds")
    print("Round each payment:", rounded_payments)
    print("Round final total:", rounded_total)
