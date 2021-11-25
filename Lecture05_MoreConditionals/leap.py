# function to check if a given year is a leap year

def isLeap(year):
    """Takes a year (int) as input and returns
    True if it is a leap year, else returns False"""

    pass # replace with code


#  following code only run when run as a script
if __name__ == "__main__":
    # ask user to enter year
    year = int(input("Enter a year: "))

    # call isLeap
    if isLeap(year): 
        print(year, "is a leap year!")
    else:
        print(year, "is not a leap year.")
