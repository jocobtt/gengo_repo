balance = 20.0
price = 21.0

# You may modify the lines of code above, but don't move them!
# When you Submit your code, we'll change these lines to
# assign different values to the variables.

# Imagine we're writing some software for a cash register or
# credit card processor. We want to approve a purchase if the
# customer's balance is greater than or equal to the purchase
# price, and reject it otherwise.
#
# Write some code below that will print True if balance is
# greater than or equal to price, and False if it is not.
def balance_check(balance, price):
    if balance > price:
        print(True)
    elif balance < price:
        print(False)
    else:
        print("Error")

balance_check(balance, price)