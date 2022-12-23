from car import Car
from motorcycle import Motorcycle
from motorcycle_adapter import MotorcycleAdapter 
import traceback

# Example from https://stackabuse.com/adapter-design-pattern-in-python/
if __name__ =='__main__':
    car = Car()
    bike = Motorcycle()
    bike_adapter = MotorcycleAdapter(bike) # Create Adapter

    print("The Motorcycle\n")
    bike.assign_rider("Saleh")
    bike.rev_throttle()
    bike.pull_brake_lever()
    print('\n')

    print("The Car\n")
    car.assign_driver("Ahmad")
    car.accelerate()
    car.apply_brakes()
    print("\n")

    print("Attempting to call client methods with service object\n")

    try:
        bike_adapter.assign_driver("Mohammad")
        bike_adapter.accelerate()
        bike_adapter.apply_brakes()
    except AttributeError:
        print("Oops! bike object cannot access car methods")
        traceback.print_exc()