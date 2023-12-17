from customers import Customers
from resturant import Restaurants

if __name__ == "__main__":
    cusFirstName = input("Enter First Name: ")
    cusFamilyName = input("Enter Family Name: ")
    person = Customers(cusFirstName, cusFamilyName)

    restaurant_name = input("Enter Restaurant Name: ")
    rating = int(input("Enter Rating (1 to 5): "))
    person.add_review(restaurant_name, rating)

    # Write reviews to a file
    with open("reviews.txt", "a") as file:
        for review in person.get_reviews():
            file.write(f"Customer: {person.fullName()}, Restaurant: {review.restaurant_name()}, Rating: {review.rating()}\n")

    print("Review has been stored in the 'reviews.txt' file.")

    restaurant_instance = Restaurants.get_or_create(restaurant_name)
    print("Restaurant Reviews:")
    for review in restaurant_instance.reviews():
        print(f"Customer: {person.fullName()}, Rating: {review.rating()}")
