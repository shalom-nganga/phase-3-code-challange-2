class Restaurants:
    _restaurant_dict = {}
    
    def __init__(self, name):
        self.__restaurant_id = len(Restaurants._restaurant_dict) + 1
        self.__restaurant_name = name
        self._reviews = []

    def restaurant_id(self):
        return self.__restaurant_id

    def name(self):
        return self.__restaurant_name
    
    def reviews(self):
        return self._reviews

    def add_review(self, review):
        self._reviews.append(review)

    @classmethod
    def get_or_create(cls, name):
        if name not in cls._restaurant_dict:
            cls._restaurant_dict[name] = cls(name)
        return cls._restaurant_dict[name]