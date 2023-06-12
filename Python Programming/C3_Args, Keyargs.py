def user_info(name, age=45, city="Oklahoma"):
    # #This function prints name, age, and city, 
    # from an argument provided to the function
    
    print("{} is {} years old, {}".format(name, age, city))

user_info("Janet", 45, "Depok")
user_info("Micah")
user_info(name="Micoh", age=55, city="Depok")

### Using *args and **kwargs

def application(fname, lname, email, company, *args, **kwargs):
    print("{} {} works at {}, and her email is {}.".format(fname, lname, company, email))

application("Jess", "Ingrass", "mail@mail.com", "Ericsson", 2500, hire_date = "September 2023")