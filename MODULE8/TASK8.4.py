#Here’s a complete implementation of the Grand Demolition Derby race simulation,
# building on the earlier car race exercise.
##It includes a Car class, a Race class, and a main program that runs the race loop.
#🏎️ Car Class
import random

class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.distance_traveled = 0

    def accelerate(self, speed_change):
        self.current_speed += speed_change
        self.current_speed = max(0, min(self.current_speed, self.max_speed))

    def drive(self, hours):
        self.distance_traveled += self.current_speed * hours
#🏁 Race Class
class Race:
    def __init__(self, name, distance_km, cars):
        self.name = name
        self.distance_km = distance_km
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)
            car.drive(1)

    def print_status(self):
        print(f"\n{'Car':<10} {'Max Speed':<10} {'Current Speed':<15} {'Distance':<10}")
        print("-" * 50)
        for car in self.cars:
            print(f"{car.registration_number:<10} {car.max_speed:<10} {car.current_speed:<15} {car.distance_traveled:<10.1f}")

    def race_finished(self):
        return any(car.distance_traveled >= self.distance_km for car in self.cars)
#🧪 Main Program
def create_cars(num_cars):
    cars = []
    for i in range(1, num_cars + 1):
        reg_number = f"ABC-{i}"
        max_speed = random.randint(100, 200)
        cars.append(Car(reg_number, max_speed))
    return cars

if __name__ == "__main__":
    # Create race
    race_name = "Grand Demolition Derby"
    race_distance = 8000
    car_list = create_cars(10)
    race = Race(race_name, race_distance, car_list)

    hours_passed = 0
    print(f"\n🏁 Starting race: {race_name} ({race_distance} km)\n")

    while not race.race_finished():
        race.hour_passes()
        hours_passed += 1

        if hours_passed % 10 == 0:
            print(f"\n⏱️ Hour {hours_passed}")
            race.print_status()

    print(f"\n🏆 Race finished in {hours_passed} hours!")
    race.print_status()
