
brunch_items = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00,
  'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00,
  'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}

early_bird_items = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00,
  'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00,
  'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}

dinner_items = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00,
  'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00,
  'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}

kids_items = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00,
  'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00,
  'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}


class Menu:

    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return "The {menu} menu is available from {start_time} to {end_time}".format(
            menu=self.name, start_time=self.start_time, end_time=self.end_time)

    def calculate_bill(self, purchase_items):
        total_bill = 0
        for purchased_item in purchase_items:
            if purchased_item in self.items:
                total_bill += self.items[purchased_item]
        return total_bill


class Franchise:

    def __init__(self, address, menus):
        self.address = address
        self.menus = menus
    
    def __repre__(self):
        return "The address of the restaurant is {add}".format(add=self.address)


flagship_store = Franchise("1232 West End Road", [brunch_items, early_bird_items, dinner_items, kids_items])
new_installement = Franchise("12 East Mulberry Street", [brunch_items, early_bird_items, dinner_items, kids_items])

brunch = Menu("brunch", brunch_items, 11, 16)

brunch_bill = brunch.calculate_bill(['pancakes', 'home fries', 'coffee'])

print(brunch_bill)
print(brunch)
print(flagship_store)
