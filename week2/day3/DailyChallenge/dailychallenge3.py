# Challenge 1
# Ask a user for a word
# Write a program that creates a dictionary. This dictionary stores the indexes of each letter in a list.

# Make sure the letters are the keys.
# Make sure the letters are strings.
# Make sure the indexes are stored in a list and those lists are values.

user_word=input('Can you give me a word: ')
letter_indexes= {}
for index,letter in enumerate(user_word):
    if letter not in letter_indexes:
        letter_indexes[letter]=[]
    letter_indexes[letter].append(index)

print(letter_indexes)


# Create a program that prints a list of the items you can afford in the store with the money you have in your wallet.
# Sort the list in alphabetical order.
# Return “Nothing” if you can’t afford anything from the store.
items_purchase = {
    "Water": "$1",
    "Bread": "$3",
    "TV": "$1,000",
    "Fertilizer": "$20"
}

wallet = 300

affordable_items = []
for item, price in items_purchase.items():
    item_price = int(price.replace('$', '').replace(',', ''))
    if item_price <= wallet:
        affordable_items.append(item)

if affordable_items:
    affordable_items.sort()
    print(affordable_items)
else:
    print("Nothing")
