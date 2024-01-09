#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = []
    if my_list:
        for num in my_list:
            new_list.append(false if num % 2 else true)
            return new_list
