class Vehicle(object):
    def __init__(self, model_year, total_mileage, vehicle_id):
        self.model_year = model_year
        self.total_mileage = total_mileage
        self.vehicle_id = vehicle_id

    def __str__(self):
        result_str = "Model year = " + str(self.model_year) + "\nMileage = " + str(self.total_mileage) + "\nVehicle " \
            "ID = " + str(self.vehicle_id) + "\n"

        return result_str


class Car(Vehicle):
    def __init__(self, model_year, total_mileage, vehicle_id, total_wheels):
        Vehicle.__init__(self, model_year, total_mileage, vehicle_id)
        self.total_wheels = total_wheels

    def __str__(self):
        result_str = Vehicle.__str__(self)
        result_str = result_str + "Wheels = " + str(self.total_wheels) + "\n"

        return result_str


class Truck(Vehicle):
    def __init__(self, model_year, total_mileage, vehicle_id, total_wheels):
        Vehicle.__init__(self, model_year, total_mileage, vehicle_id)
        self.total_wheels = total_wheels

    def __str__(self):
        result_str = Vehicle.__str__(self)
        result_str = result_str + "Wheels = " + str(self.total_wheels) + "\n"

        return result_str


veh1 = Vehicle(2018, 1080, 1234)
veh2 = Car(2012, 2000, 1243, 4)
veh3 = Truck(2015, 4027, 2134, 18)

print(veh1)
print(veh2)
print(veh3)
