class Customers:
    _id_count = 1
    
    def __init__(self, cusName, famName):
        self._customer_id = Customers._id_count
        self._customer_given_name = cusName
        self._family_given_name = famName
        Customers._id_count += 1
        self._reviews = []

    def get_cusName(self):
        return self._customer_given_name
    
    def get_famName(self):
        return self._family_given_name
    
    def fullName(self):
        return f"{self._customer_given_name} {self._family_given_name}"
    
    newName = property(get_cusName, get_famName)

    def add_review(self, restaurant_name, rating):
        from resturant import Restaurants
        restaurant_instance = Restaurants.get_or_create(restaurant_name)
        
        from review import Review
        review = Review(restaurant_instance, self, rating)
        self._reviews.append(review)
        restaurant_instance.add_review(review)

    def get_reviews(self):
        return self._reviews
    
    def get_id(self):
        return self._customer_id