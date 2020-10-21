"""
Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.

The year can be evenly divided by 4, is a leap year, unless:
    The year can be evenly divided by 100, it is NOT a leap year, unless:
        The year is also evenly divisible by 400. Then it is a leap year.
"""

def is_leap(year):
    leap = True

    # Write your logic here
    if (year % 4 == 0):
        result = leap
        if (year % 100 == 0):
            result = not leap
            if (year % 400 == 0):
                result = leap
    else:
        result = not leap
    print(result)

if __name__ == "__main__":
    year = int(input())
    is_leap(year)