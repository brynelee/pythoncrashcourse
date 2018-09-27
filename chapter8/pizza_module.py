#! /usr/bin/python3

# 演示传递任意数量的实参，*toppings会代表任意数量的实参，自动转换成元祖tuple
def make_pizza(*toppings):
    """print all toppings"""
    print(toppings)

# using loop for tuple
def make_pizza_loop(*toppings):
    """print all toppings"""
    for topping in toppings:
        print('- ' + topping)


# 演示使用位置实参和任意数量实参
def make_pizza_with_size(size, *toppings):
    """概述要制作的pizza"""
    print('\nMaking a ' + str(size) + '-inch pizza with the following toppings:')
    for topping in toppings:
        print('- ' + topping)


