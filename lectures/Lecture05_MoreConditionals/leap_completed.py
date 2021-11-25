# function to check if a given year is a leap year

def isLeap(year):
    """Takes a year (int) as input and returns
    True if it is a leap year, else returns False"""

    # if not divisible by 4 return False
    if year % 4 != 0:
        return False

    # is divisible by 4 but not divisible by 100
    elif year % 100 != 0:
        return True

    # is divisible by 4 and divisible by 100
    # but is not divisible by 400
    elif year % 400 != 0:
        return False

    # is divisible by 400 (and also 4, and 100)
    return True


#  following code only run when run as a script
if __name__ == "__main__":
    # ask user to enter year
    year = int(input("Enter a year: "))

    # call isLeap
    if isLeap(year):
        print(year, "is a leap year!")
    else:
        print(year, "is not a leap year.")
