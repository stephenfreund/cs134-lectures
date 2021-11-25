# simple function to make change
# module change

def numCoins(cents):
  """Takes as input cents and returns
  the fewest number of coins of type
  quarter, dimes, nickels and pennies
  that can make change for cents"""
  q = cents // 25 # num of quarters
  cents = cents % 25 # rest
  d = cents // 10 # number of dimes
  cents = cents % 10 # what is left
  n = cents // 5 # number of nickels
  p = cents % 5 # number of pennies
  print("{} quarters, {} dimes, {} nickels, {} pennies".format(q, d, n, p))
  return q + d + n + p

# call the function here

if __name__ == "__main__":
  cents = int(input("Enter the number of cents: "))
  print("Number of coins: ", numCoins(cents))



  
