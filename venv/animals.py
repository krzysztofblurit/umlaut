from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.__name=name

    @property
    def name(self):
        return self.__name

    def introduction(self):
        print ("My name is {0}, I am a {1}".format(self.__name, self.__class__.__name__))
        # print (self.__name)

    @abstractmethod
    def sound(self):
        pass
    @abstractmethod
    def travel(self):
        pass

class FlyingAnimal(Animal):
    def __init__(self, name):
        super().__init__(name)
    def _fly(self):
        print("it's flying")

class SwimmingAnimal(Animal):
    def __init__(self, name):
        super().__init__(name)
    def _swim(self):
        print("It's swimming")

class RunningAnimal(Animal):
    def __init__(self, name):
        super().__init__(name)
    def _run(self):
        print("It's running")

class Duck(FlyingAnimal, SwimmingAnimal, RunningAnimal):
    def __init__(self, name):
        super().__init__(name)
    def sound(self):
        print("Quack")
    def travel(self):
        super()._run()
        super()._fly()
        super()._swim()

class PolarBear(SwimmingAnimal, RunningAnimal):
    def __init__(self, name):
        super().__init__(name)
    def sound(self):
        print("Roar")
    def travel(self):
        super()._run()
        super()._swim()

class FlyingPolarBear(PolarBear, FlyingAnimal):
    def __init__(self, name):
        super().__init__(name)
    def _fly(self):
        super()._fly()
        print("with magic")
    def sound(self):
        print("Roar")
    def travel(self):
        super().travel()
        self._fly()

def main():

    kaczka = Duck("McKwak")
    misiek = PolarBear("PedoBear")
    magicznyMisiek = FlyingPolarBear("Yogi")

    animals_list = []
    animals_list.append(kaczka)
    animals_list.append(misiek)
    animals_list.append(magicznyMisiek)

    for animal in animals_list:
        animal.introduction()
        animal.sound()
        animal.travel()


if __name__ == "__main__":
    main()