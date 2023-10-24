


class Customer:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def given_name(self):
        return self
        
    def family_name(self):
        return self.last_name
    def full_name(self):
        return [self.first_name, self.last_name]
    def all():
        pass


class Restaurant:
    def __init__(self, name):
        self.name = name
    def name(self):
        return self.name
    

class Review:
    pass