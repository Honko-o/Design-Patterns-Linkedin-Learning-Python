from abc import ABC

# Interface
class Drone(ABC):
    def beep(self):
        pass
    def spin_rotators(self):
        pass
    def take_off(self):
        pass