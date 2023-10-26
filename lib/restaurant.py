

class Customer:
    list = []
    
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

        Customer.list.append(self)
    
    def given_name(self):
        return self.first_name
        
    def family_name(self):
        return self.last_name
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
   
    @classmethod
    def all(cls):
        return cls.list
    
    def __repr__(self):
        return f"{self.first_name} {self.last_name}"
    
customer1 = Customer("Smith", "AbdulHakeem")
customer2 = Customer("John", "Olakunle")

print(Customer.list)
print(customer1.full_name())

class Restaurant:
    def __init__(self, name):
        self.name = name
        self.reviews = []
    
    def name(self):
        return self.name
    
    def review(self):
        return self.reviews
    
    def customers():
        return Customer.list
    
restaurant1 = Restaurant("Sweet Sensation")
restaurant2 = Restaurant("Salado")
    

class Review:
    all_reviews = []

    def __init__(self, customer, restaurant, ratings=0):
        self.customer = customer
        self.restaurant = restaurant
        self.ratings = ratings

        Review.all_reviews.append(self)
    def rating(self):
        return self.ratings
    
    def restaurants(self):
        return self.restaurant
    
    def all(cls):
        return cls.all_reviews
    pass

review1 = Review(customer1, restaurant1, 2 )