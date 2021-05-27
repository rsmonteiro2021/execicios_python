from restaurant import Restaurant, IceCreamStand

restaurant = Restaurant('Xian', 'Chinesa')
restaurant = IceCreamStand('Xian', 'Chinesa')
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.number_served = 25
restaurant.set_number_served()
restaurant.increment_number(150)
restaurant.show_flavors()