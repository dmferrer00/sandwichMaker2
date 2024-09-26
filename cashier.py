class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        coins = input("How many quarters?: ")
        coins = float(coins)
        total = coins * .25
        return total

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins < cost:
            print("Sorry, that’s not enough money. Money refunded.")
            print("You need " + str(cost - coins) + " more." )
            return False
        else:
            change = round(coins - cost, 2)
            print("Here is your change $" + str(coins - cost) + ".")
            return True