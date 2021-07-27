# -*- coding: utf-8 -*-
# filename ~/sbox/LPTHW/mystuff/ex4.py

cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven + space_in_a_car
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("there are only", drivers, "drivers available.")
print("threre will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "space_in_a_car")


stones = 6
space_in_gauntlet = 6.0
snappers = 3
avengers = 30
stones_not_used = 0
snap_destruction = 2.0
all_sentient_life = 100000000000.0
snap_capacity = all_sentient_life / snap_destruction
average_death_per_stone = snap_capacity / stones


print("There are", stones, "stones available.")
print("There are only", snappers, "people who will snapp.")
print("There will be", stones_not_used, "empty gauntlet sockets.")
print("We can erase", snap_capacity, "people today.")
print("we have", avengers, "to snapp today.")
print("We need to put about", average_death_per_stone, "space_in_gauntlet")


"""
rewritten, change space to seats and construct a car from python

create as many pieces as you can of a car.

test user menu to open badwords.json and test they are there to be suppressed
top 10 worse phrases by severity
"""