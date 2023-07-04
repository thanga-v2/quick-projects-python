messgae="this is an experiment of string datatypes in pyhton"

print("actual message - ",messgae)
print("modified -",messgae.title())
print("hashed -",messgae.__hash__())

message = "test the new hashed built in variable"
hashed_message = message.__hash__()
print(hashed_message)
print(hashed_message.__hash__())
print(hashed_message.__hash__())


# what is 'f' strings in python?
# 'f' means format - python formats the string by placing the variables in braces {}

car_make = "BMW"
car_model = "5er 2018"
car = f"{car_make} and {car_model}"
print(car)
my_message = f"thanga loves to drive {car.upper()}. but he can't"
print(my_message)


# Understanding tabs and white spaces

print("this is a \t in my message")
message="testing the tab"
inputsample="hope you got the sample"
letstab=f"incl tab {message}\t{inputsample}"
print("tab with f string",letstab)
# print("tab without f string - ",{messgae} \t {inputsample})
print("values with \t tab, \n one \n two \n three")
print("python")
print("python ")

# r strip will remove the extra white spaces of a string in the right side.
myfavlanguage = 'python '
mysecfavlanguage = ' python'
print(myfavlanguage)
print(myfavlanguage.rstrip())
print(mysecfavlanguage.lstrip())

# remove_prefix
# this will remove the prefix in an URL
facebookurl = "https://www.facebook.com"
print(facebookurl.removeprefix("https://"))


mymessage = "this is the best course to read about python's functionality"
mynewmessage = "this is the best course to read about python\"s functionality"
mysecnewmessage = 'this is the best course to read about python\'s functionality'
print(mymessage)
print(mynewmessage)
print(mysecnewmessage)

