from drone import Drone

class SuperDrone(Drone):
    def beep(self):
        print('Beep beep beep')
    
    def spin_rotators(self):
        print("Rotators are spinning")

    def take_off(self):
        print('Taking off')

    