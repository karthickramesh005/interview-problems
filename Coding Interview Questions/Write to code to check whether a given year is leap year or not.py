# Write to code to check whether a given year is leap year or not. :

def is_leap_year(year):
    # Leap years are either divisible by 4 but not divisible by 100,
    # or divisible by 400.
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Example usage:
year_to_check = int(input("Enter a year : ")) # You can change this to any year

if is_leap_year(year_to_check):
    print(f"{year_to_check} is a leap year.")
else:
    print(f"{year_to_check} is not a leap year.")
