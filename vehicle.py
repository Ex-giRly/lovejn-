class vehicle:

    def __init__(self, max_speed, mileage):

             self.max_speed = max_speed
             self.mileage = mileage

modelx = vehicle(240, 25)
modely = vehicle(300, 15)

print("modelx max speed and mileage respectively: ", modelx.max_speed, "and", modelx.mileage)

print("modely max speed and mileage respectively: ", modely.max_speed, "and", modely.mileage)