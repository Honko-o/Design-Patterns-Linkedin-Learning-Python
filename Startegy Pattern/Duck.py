from abc import abstractmethod, ABC

# Interface
class FlyBehavior(ABC):
    @abstractmethod
    def fly():
        pass
# Interface
class QuackBehavior(ABC):
    @abstractmethod
    def quack():
        pass

class FlyWithWings(FlyBehavior):
    def fly():
        print("I'm Flying")
class FlyNoWay(FlyBehavior):
    def fly():
        print("I can't fly")
class Quack(QuackBehavior):
    def quack():
        print("Quack")
class Squeak(QuackBehavior):
    def quack():
        print("Squeak")
class Silence(QuackBehavior):
    def quack():
        print("I can't Quack")

class Duck (ABC):
    # Constructor
    def __init__(self):
        self.flyBehavior = FlyBehavior
        self.quackBehavior = QuackBehavior
        

    @abstractmethod
    def display(self):
        pass

    def performFly(self):
        self.flyBehavior.fly()
    def performQuack(self):
        self.quackBehavior.quack()
    def swim():
        print("All ducks float, even decoys!")
    def setFlyBehavior(self):
        pass
    def setQuackBehavior(self):
        pass


class MallardDuck(Duck):
    def __init__(self):
        self.flyBehavior = FlyWithWings
        self.quackBehavior = Quack
    
    def display(self):
        print("I am real Mallard Duck")
    

mallard = MallardDuck()
mallard.performFly()
mallard.performQuack()