class Review:
    _review_id_counter = 1
    
    def __init__(self, restaurant, customer, rating):
        self.__restaurant = restaurant
        self.__customer = customer
        self.__rating = rating
        self.__review_id = Review._review_id_counter
        Review._review_id_counter += 1

    def customer_id(self):
        return self.__customer.get_id()
    
    def restaurant_id(self):
        return self.__restaurant.restaurant_id()

    def rating(self):
        return self.__rating
    
    def review_id(self):
        return self.__review_id
    
    def customer_name(self):
        return self.__customer.fullName() 
    
    def restaurant_name(self):
        return self.__restaurant.name() 
