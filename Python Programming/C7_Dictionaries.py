stuff = {"food": 15, "energy": 100, "enemies":3}

# # Get Value
# print(stuff.get("food"))

# # Get items / both Keys and its value
# print(stuff.items())

# # Get Keys / Keywords only 
# print(stuff.keys())

# Pop item
# print(stuff.popitem())
# print(stuff)

# # Setting the default
# print(stuff.setdefault("food"))
# print(stuff)

# # Adding Keys and Value to the default
# print(stuff.setdefault("friends", 123))
# print(stuff)

new_items = {"rocks": 4, "arrows": 18}
stuff.update(new_items)
print(stuff)

new_items = {"rocks": 5, "arrows": 19}
stuff.update(new_items)
print(stuff)

up_new = {"food": 3, "webs": 2}
stuff.update(up_new)
print(stuff)

stuff.update(food = 450, cookies = 6)
print(stuff)
