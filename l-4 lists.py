# what are lists?
# lists is very imp concepts in pyhton
# lists is a collection of items in a particular order. eg, names, age, marks etc..
# best way is defining the  lists in plural

car_makes = ["mercedes", "bmw ", "ferrari", "honda", "kia", "hyundai", "skoda", "volkswagen", "range rover"]
print(car_makes)
# printing the first element in the list
print(car_makes[0])
# to access the value in a list, we must access with the help of index
print(car_makes[1].rstrip())
print(car_makes[1].upper())

# printing the last element in the list = -1
print(car_makes[-1])

# printing the middle element in list
middle = len(car_makes)/2
# without floor
print(f"middle element of list is\t{middle}")
# with floor
print(f"middle element of list is\t{middle.__floor__()}")
print(car_makes[middle.__floor__()])

print(f"Im hoping to get my first car soon. {car_makes[7]}")


# Modifying an element in the list
print("before modified\t", car_makes)
car_makes[5] ="modified_car_surprise"
print("after modified\t", car_makes)

# Pop the elements
car_poped = car_makes.pop()
print(f"car popped {car_poped}")
print("after pop ->",car_makes)

# pop by index

print(f"before we pop by index\t{car_makes}")
pop_by_index=car_makes.pop(1)
print(f"poped car\t{pop_by_index}")
print(f"results after\t{car_makes}")

# remove by remove
# we can also remove like the below mentioned way

car_makes.remove("modified_car_surprise")
print(f"after removed\t{car_makes}")
car_makes.sort(reverse=False)
print(f"sorted one\t{car_makes}")
car_makes.sort(reverse=True)
print(f"sorted one\t{car_makes}")

# we can also print this way
# by default the sort is ascending
print(sorted(car_makes))

