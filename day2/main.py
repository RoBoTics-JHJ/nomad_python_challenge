"""
As you can see, the code is broken.
Create the missing functions, use default arguments.
Sometimes you have to use 'return' and sometimes you dont.
Start by creating the functions
"""


def is_on_list(days_list, day='Wed'):
    if day in days_list:
        return True
    else:
        return False


def get_x(days_list, index=3):
    return days_list[index]


def add_x(days_list, add_day='Sat'):
    days_list.append(add_day)


def remove_x(days_list, remove_day='Mon'):
    days_list.remove(remove_day)


# \/\/\/\/\/\/\  DO NOT TOUCH AREA  \/\/\/\/\/\/\ #

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

print("Is Wed on 'days' list?", is_on_list(days, "Wed"))

print("The fourth item in 'days' is:", get_x(days, 3))

add_x(days, "Sat")
print(days)

remove_x(days, "Mon")
print(days)

# /\/\/\/\/\/\/\ END DO NOT TOUCH AREA /\/\/\/\/\/\/\ #
