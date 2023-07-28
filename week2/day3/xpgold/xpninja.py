a = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet"
my_list = a.split(",")
# print(f"This is how many companies are in the list {len(my_list)}")
my_list.sort()
my_list.reverse()
# print(my_list)
list_with_o = [x for x in my_list if "o" in x]
# print(list_with_o)
list_without_i = [x for x in my_list if "i" not in x]
# print(list_without_i)

# Bonus
other_list = ["Honda","Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"] 
set_list = set(other_list)

# print(set_list)

# Bonus

sorted_manufacturers = sorted([other_list[::-1] for other_list in set(other_list)])

for manufacturer in sorted_manufacturers:
    print(manufacturer)



