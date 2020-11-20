# List manager

def random_order(a_list):
    return list

def order_by_increasing_value(a_list):
    '''returns the list ordered by increasing value'''
    pass

def order_by_decreasing_value(a_list):
    '''returns the list ordered by decreasing value'''
    pass

def reverse_order(a_list):
    '''returns the list in reverse order'''
    pass

def stringfy_list(a_list):
    '''returns a list with all elements turned into strings'''
    return str(a_list)

def multiply_list(a_list, a):
    '''returns the list with all elements multipled by the value multiple'''
    a_list = [_*a for _ in a_list]
    return a_list

def get_highest_value(a_list):
    '''returns the highest value of the list'''
    a_list.sort(reverse=True)
    return a_list[:1]

def get_lowest_value(a_list):
    '''returns the lowest value of the list'''
    a_list.sort()
    return a_list[:1]

print(stringfy_list([1,2,3]))