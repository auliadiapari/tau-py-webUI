# Lists


class Lists:
    fruits = ["grapes", "banana", "apples", "apples", "dragonfruit"]
    years = ["1997", "1998", "2023", 1995, 2024]
    # print(fruits, years)

    # #Append
    # fruits.append("oranges") # Adding new objects to the list
    # print(fruits)

    # #Extend
    # fruits.extend(years)
    # print(fruits)

    # #Remove by remove
    # fruits.remove("oranges") #the value/object need to exact match, if not, will cause an error
    # print(fruits)

    # #Remove by index
    # fruits.pop(0) #will remove the value by index
    # print(fruits)

    # #Remove by negative indexing (start at the end of the list)
    # fruits.pop(-1)
    # print(fruits)

    # #Sorts
    # numbers = [10, 20, 40, 30, 35]
    # numbers.sort()
    # print(numbers)

class Lists_Check_Membership:
    # In
    print("apple" in Lists.fruits) #not exact match
    print("apples" in Lists.fruits) #exact match
    
    # Counts
    print(Lists.fruits.count("apples"))
    print(Lists.fruits.count("apple"))

    # Index
    print(Lists.fruits.index("apples"))




