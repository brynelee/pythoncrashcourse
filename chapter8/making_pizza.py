import pizza_module

pizza_module.make_pizza('pepperoni')
pizza_module.make_pizza('mushrooms', 'green peppers', 'extra cheese')

print('====================')

pizza_module.make_pizza_loop('pepperoni')
pizza_module.make_pizza_loop('mushrooms', 'green peppers', 'extra cheese')

print('====================')

pizza_module.make_pizza_with_size(16, 'pepperoni')
pizza_module.make_pizza_with_size(12, 'mushrooms', 'green peppers', 'extra cheese')