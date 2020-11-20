# List manager
import random

def random_order(a_list):
    random.shuffle(a_list)
    return a_list

def order_by_increasing_value(a_list):
    '''returns the list ordered by increasing value'''
    a_list.sort()
    return a_list

def order_by_decreasing_value(a_list):
    '''returns the list ordered by decreasing value'''
    a_list.sort(reverse=True)
    return a_list

def reverse_order(a_list):
    '''returns the list in reverse order'''
    reversed = [a_list[_] for _ in range(len(a_list)-1, -1, -1)]
    return reversed

def stringfy_list(list):
    '''returns a list with all elements turned into strings'''
    pass

def multiply_list(list, multiple):
    '''returns the list with all elements multipled by the value multiple'''
    pass

def get_highest_value(list):
    '''returns the highest value of the list'''
    pass

def get_lowest_value(list):
    '''returns the lowest value of the list'''
    pass