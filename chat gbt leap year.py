def is_leap_year(year):
    # Check if the year is divisible by 4
    if year % 4 == 0:
        # If divisible by 100, check if it's divisible by 400
        if year % 100 == 0:
            if year % 400 == 0:
                return True  # Leap year
            else:
                return False  # Not a leap year
        else:
            return True  # Leap year
    else:
        return False  # Not a leap year

# Input: ask the user for a year
year = int(input("Enter a year: "))

# Output: check and print whether it's a leap year
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
