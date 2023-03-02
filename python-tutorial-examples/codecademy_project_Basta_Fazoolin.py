
brunch_items = {
    'pancakes': 7.50,
    'waffles': 9.00,
    'burger': 11.00,
    'home fries': 4.50,
    'coffee': 1.50,
    'espresso': 3.00,
    'tea': 1.00,
    'mimosa': 10.50,
    'orange juice': 3.50
}

early_bird_items = {
    'salumeria plate': 8.00,
    'salad and breadsticks (serves 2, no refills)': 14.00,
    'pizza with quattro formaggi': 9.00,
    'duck ragu': 17.50,
    'mushroom ravioli (vegan)': 13.50,
    'coffee': 1.50, 'espresso': 3.00,
}


dinner_items = {
    'crostini with eggplant caponata': 13.00,
    'caesar salad': 16.00,
    'pizza with quattro formaggi': 11.00,
    'duck ragu': 19.50,
    'mushroom ravioli (vegan)': 13.50,
    'coffee': 2.00,
    'espresso': 3.00,
}

kids_items = {
    'chicken nuggets': 6.50,
    'fusilli with wild mushrooms': 12.00,
    'apple juice': 3.00
}

arepa_items = {
    'arepa pabellon': 7.00,
    'pernil arepa': 8.50,
    'guayanes arepa': 8.00,
    'jamon arepa': 7.50
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


brunch = Menu('Brunch', brunch_items, 1100, 1600)
early_bird = Menu('Early Bird', early_bird_items, 1500, 1800)
dinner = Menu('Dinner', dinner_items, 1700, 2300)
kids = Menu('Kids', kids_items, 1100, 2100)
arepa = Menu('Take a Arepa', arepa_items, 1000, 2000)


class Franchise:

    def __init__(self, address, menus):
        self.address = address
        self.menus = menus

    def __repr__(self):
        return "The address of the restaurant is {add}.".format(add=self.address)

    def available_menus(self, time):
        available_menus = []
        for menu in self.menus:
            if time >= menu.start_time and time <= menu.end_time:
                available_menus.append(menu)
        return available_menus


flagship_store = Franchise('1232 West End Road', [
                           brunch, early_bird, dinner, kids])
new_installement = Franchise('12 East Mulberry Street', [
                             brunch, early_bird, dinner, kids])
arepa_franchise = Franchise('189 Fitzgerald Avenue', [arepa])


class Bussiness:
    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises


basta_bussiness = Bussiness("Basta Fazoolin' with my heart", [
    flagship_store, new_installement])
arepa_bussiness = Bussiness('Take a Arepa', [arepa_franchise])


# tests
brunch_bill = brunch.calculate_bill(['pancakes', 'home fries', 'coffee'])
kids_bill = kids.calculate_bill(
    ['pancakes', 'fusilli with wild mushrooms', 'coffee'])

print(brunch_bill)
print(kids_bill)
print(brunch)
print(kids)
print(flagship_store)

print(flagship_store.available_menus(1800))
print(arepa_bussiness.franchises[0].menus[0])
