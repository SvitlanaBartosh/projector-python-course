class Restaurant:
    def __init__(self,name, cuisine, menu):
        self.name = name
        self.cuisine = cuisine
        self.menu = menu

class FastFood(Restaurant):
    def __init__(self, name, cuisine, menu, drive_thru):
        super().__init__(name, cuisine, menu)
        self.drive_thru = drive_thru

    def order(self, dish, quantity_order):
        if self.menu.get(dish) is None:
            return 'Dish not available'
        if self.menu.get(dish)['quantity'] < quantity_order:
            return 'Requested quantity not available'
        if self.menu.get(dish)['quantity'] >= quantity_order:
           return quantity_order * self.menu.get(dish)['price']
        

menu =  {
    'burger': {'price': 5, 'quantity': 10},
    'pizza': {'price': 10, 'quantity': 20},
    'drink': {'price': 1, 'quantity': 15}   
}

mc = FastFood('McDonalds', 'Fast Food', menu, True)

assert mc.order('burger', 5) == 25
assert mc.order('burger', 15) == 'Requested quantity not available'
assert mc.order('soup', 5) == "Dish not available"