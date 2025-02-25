def order(dish):
    return"your order: " + dish
def process_order(dish, func):
    print(func(dish))
    process_order("fish", order)