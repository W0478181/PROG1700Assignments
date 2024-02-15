class Person:
    def __init__(self,first_name,last_name,mobile,email):
        self.first_name = first_name
        self.last_name = last_name
        self.mobile = mobile
        self.email = email
    def make_trip(self,route):
        print(f"{self.first_name,self.last_name} is making a trip along the route: {route}.")
 
class Driver(Person):
    def __init__(self, first_name, last_name, mobile, email, v_make, v_model, v_color, v_type):
        super().__init__(first_name, last_name, mobile, email)
        self.v_make = v_make
        self.v_model = v_model
        self.v_color = v_color
        self.v_type = v_type
    def make_trip(self, route):
        print(f"\n{self.first_name} {self.last_name} is driving a {self.v_color} {self.v_make} {self.v_model} {self.v_type}, Leaving from {route[0]}, stopping at {route[1]} arriving at {route[len(route) - 1]}")

class Rider(Person):
    def __init__(self, first_name, last_name, mobile, email):
        super().__init__(first_name, last_name, mobile, email)

    def make_route(self, route, choise):
        print(f"\n{self.first_name} {self.last_name}, Where would you like {driver1.first_name} {driver1.last_name} to meet you.")
        choise = input("Enter Antigonish, Arena or Bayside:")
        if choise in routes[1]:
            return route



    def make_trip(self, route):
        print(f"\n{self.first_name} {self.last_name}, {driver1.first_name} {driver1.last_name} will pick you up at {route[1]}.")

driver1 = Driver("Dyan","Bryan","902-420-6969","Dbryan@yahoo.com","Nissan","Sentra","Black","car")
rider1 = Rider("Paul","Blart","902-123-4567","PB@yahoo.com")

routes = {
    1: {"PickUp":["Antigonish", "Arena", "Bayside",]},
    2: {"Stops":["Antigonish", "Bayside", "Arena"]},
    3: {"Destination":["Antigonish", "Bayside", "Arena", "Strait Area"]}
}

driver1.make_trip(route)
rider1.make_trip(route)