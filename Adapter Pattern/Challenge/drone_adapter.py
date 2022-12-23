
class DroneAdapter:
    def __init__(self, drone):
        self.drone = drone
    
    # Duck Methods
    def quack(self):
        self.drone.beep()
    
    def fly(self):
        self.drone.take_off()