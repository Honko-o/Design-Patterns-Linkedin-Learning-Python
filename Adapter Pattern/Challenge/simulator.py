import traceback
from drone import Drone
from super_drone import SuperDrone
from drone_adapter import DroneAdapter
from duck import Duck
from mallard_duck import MallardDuck


if __name__ == '__main__':
    super_drone = SuperDrone()
    mallard_duck = MallardDuck()
    # Duck Methods will be available for drone to use now let's try it
    drone_adapter = DroneAdapter(super_drone)

    try:
        drone_adapter.fly()
        drone_adapter.quack()
    except AttributeError:
        print("Oops! bike object cannot access car methods")
        traceback.print_exc()