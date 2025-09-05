lass Vehicle:
    def move(self):

class Car(Vehicle):
    def move(self):
        print("Driving on the road!")

class Plane(Vehicle):
    def move(self):
        print(" Flying in the sky!")

class Boat(Vehicle):
    def move(self):
        print("Sailing on the water!")

class Bicycle(Vehicle):
    def move(self):
        print("Pedaling on the street!")


vehicles = [Car(), Plane(), Boat(), Bicycle()]

for v in vehicles:
    v.move()
