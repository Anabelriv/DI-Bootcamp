class MenuManager:
    def __init__(self):
        self.menu = [
    {
        "name": "Soup",
        "price":10, 
        "spice":"B",
        "gluten":False
    },
    {
        "name": "Hamburger",
        "price": 15, 
        "spice": "A", 
        "gluten": True
    },
    {   
        "name": "Salad", 
        "price": 18, 
        "spice": "A", 
        "gluten": False
    },
    {
        "name": "French Fries", 
        "price": 5, 
        "spice": "C", 
        "gluten": False
    },
    {
        "name": "Beef bourguignon", 
        "price": 25, 
        "spice": "B", 
        "gluten": True
    }]

    def add_item(self,name, price, spice, gluten):
        new_dish = {"name": name, "price": price, "spice": spice, "gluten": gluten}
        self.menu.append(new_dish)

    def update_item(self,name, price, spice, gluten):
        for dish in self.menu:
            if dish["name"] == name:
                dish["price"] = price
                dish["spice"] = spice
                dish["gluten"] = gluten
                return
        print(f"{name} is not in the menu.")

    def remove_item(self,name):
        for dish in self.menu:
            if dish["name"] == name:
                self.menu.remove(dish)
                print(f"{name} has been removed.")
                return
        print(f"{name} is not in the menu.")

# spice_level = {
#     "A" : "not spicy",
#     "B" : "a little spicy",
#     "C" : "very spicy"
# }

# Create a MenuManager object
manager = MenuManager()

manager.add_item("Pizza", 20, "B", True)

manager.update_item("Salad", 22, "B", False)

manager.remove_item("Hamburger")

print(manager.menu)
