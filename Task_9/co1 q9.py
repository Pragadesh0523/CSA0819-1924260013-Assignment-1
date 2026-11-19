
def calculator(fat, snf):
    # Allowed input ranges
    MIN_FAT = 0.0
    MAX_FAT = 10.0
    MIN_SNF = 0.0
    MAX_SNF = 15.0

    if fat < MIN_FAT or fat > MAX_FAT:
        raise ValueError("Fat percentage is outside the allowed range")

    if snf < MIN_SNF or snf > MAX_SNF:
        raise ValueError("SNF percentage is outside the allowed range")

    # Calculate total solids
    total_solids = fat + snf

    return total_solids


def test_calculator():
    # Normal and boundary test cases
    assert calculator(4.0, 9.0) == 13.0
    assert calculator(3.0, 8.0) == 11.0
    assert calculator(5.0, 9.0) == 14.0
    assert calculator(3.5, 8.5) == 12.0
    assert calculator(0.0, 8.5) == 8.5
    assert calculator(10.0, 8.5) == 18.5

    # Invalid input tests
    try:
        calculator(-1.0, 8.5)
        assert False, "Negative fat should be rejected"
    except ValueError:
        pass

    try:
        calculator(11.0, 8.5)
        assert False, "Fat above maximum should be rejected"
    except ValueError:
        pass

    try:
        calculator(3.5, -1.0)
        assert False, "Negative SNF should be rejected"
    except ValueError:
        pass

    print("All automated tests passed!")


if __name__ == "__main__":
    test_calculator()

    fat = float(input("Enter fat percentage: "))
    snf = float(input("Enter SNF percentage: "))

    try:
        result = calculator(fat, snf)
        print("Total solids:", result, "%")
    except ValueError as e:
        print("Error:", e)
