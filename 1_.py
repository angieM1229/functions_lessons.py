# def happy_birthday(name, age): # parameter
#     print(f"Happy birthday to {name}!")
#     print(f"You are {age} years old!")
#     print(f"Happy birthday to you {name}!")
     
# happy_birthday("Sis", 20) # this is how you call/invoke the function  -arguement
# happy_birthday("Steve", 30)
# happy_birthday("Joe", 40)

# def display_invoice(username, amount, due_date):
#     print(f"Hello {username}")
#     print(f"Your bill of ${amount:.2f} is due: {due_date}")

# display_invoice( "Brocode", 42.50, "01/01")
# # return = statement used to end a function
# #       and send a result back ti the caller

# def add(x,y):
#     z= x+y
#     return z

# def subtract(x,y):
#     z= x-y
#     return z
# def multiply (x,y):
#     z= x*y
#     return z
# def divide (x,y):
#     z= x/y
#     return z

# print(add(1,2))
# print(subtract(1,2))
# print(multiply(1,2))
# print(divide(1,2))

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + "" + last
full_name = create_name("Angela")