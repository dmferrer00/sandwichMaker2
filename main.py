import data
from sandwich_maker import SandwichMaker
from cashier import Cashier

# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()

def main():
    while True:
        choice = input("What would you like? (small/ medium/ large/ off/ report): ")
        if choice == "off":
            exit()
        if choice == "report":
            print(resources)
        elif choice == recipes["small", "medium", "large"]:
            sandwich = recipes[choice]
            if sandwich_maker_instance.check_resources(sandwich['ingredients']):
                coins_inserted = cashier_instance.process_coins()
                if cashier_instance.transaction_result(coins_inserted, sandwich['cost']):
                    sandwich_maker_instance.make_sandwich(choice, sandwich['ingredients'])
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()
