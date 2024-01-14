#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = []
    if my_list:
        for number in my_list:
            if number % 2:
                new_list += number
    return (new_list)
