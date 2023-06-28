# Ligatures

print(10 == 10)

print("sachin" == 'sachin')

print(10 <= 10)


def test_func():
    print("basic function definition")
    return "sachin"


# Note -
# print inside the function gets called when we assign the function
# return gets called when we access the variable
testfunc = test_func()
print(f"basic function call {testfunc}")


def main():
    print("inside the main function")
    # Note -
    # Using ligatures in a variable name
    var = 42
    print(var)

    # Note -
    # Using ligatures in a function name


def greet(name):
    print(f"hello {name}")


greet("thanga")


def normal():
    return "normal"


normal()

# Note -
# Using ligatures in a conditional statement
if 5 + 5 >= 10:
    print("ligatures in a conditional statement")

# Note -
# Using ligatures in a list comprehension
numbers = [1, 2, 3, 4, 5]
squares = [num ** 2 for num in numbers]
print(squares)

main()
