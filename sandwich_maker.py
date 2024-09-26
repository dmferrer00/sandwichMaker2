
class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for i in ingredients:
            if ingredients[i] > self.machine_resources.get(i):
                print("not enough resources, need more" + i)
                return False
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        for i in order_ingredients:
            self.machine_resources[i] -= order_ingredients[i]
        print("Your " + sandwich_size +  " sandwich is ready.")