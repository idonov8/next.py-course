class Animal():
    """
    A class used to represent an animal
	"""
    def __init__(self, name, hunger=0):
        self._name = name
        self._hunger = hunger
        self._zoo_name = "Hayaton"
    
    def get_name(self):
        return self._name
    
    def is_hungry(self):
        return self._hunger > 0
    
    def feed(self):
        self._hunger -= 1

    def talk(self, words):
        print(words)    

class Dog(Animal):
    def talk(self):
        super().talk("woof woof")
    
    def fetch_stick(self):
        print("There you go, sir!	")

class Cat(Animal):
    def talk(self):
        super().talk("meow")
    
    def chase_laser(self):
        print("Meeeeow")

class Skunk(Animal):
    def __init__(self, name, hunger, stink_count=6):
        super().__init__(self, name, hunger)
        self._stink_count = stink_count

    def talk(self):
        super().talk("tsssss")
    
    def stink(self):
        print("Dear lord!")

class Unicorn(Animal):
    def talk(self):
        super().talk("Good day, darling")
    
    def sing(self):
        print("I’m not your toy...")

class Dragon(Animal):
    def __init__(self, name, hunger, color="Green"):
        super.__init__(self, name, hunger)
        self._color = color

    def talk(self):
        super().talk("Raaaawr")
    
    def breath_fire(self):
        print("$@#$#@$")


def main():
    zoo_lst = []
    zoo_lst.append(Dog("Brownie", 10))
    zoo_lst.append(Cat("Zelda", 3))
    zoo_lst.append(Skunk("Stinky"))
    zoo_lst.append(Unicorn("Keith", 7))
    zoo_lst.append(Dragon("Lizzy", 1450))

    zoo_lst.append(Dog("Doggo", 80))
    zoo_lst.append(Cat("Kitty", 80))
    zoo_lst.append(Skunk("Stinky Jr.", 80))
    zoo_lst.append(Unicorn("Clair", 80))
    zoo_lst.append(Dragon("McFly", 80))
    
    for animal in zoo_lst:
        print(str(animal.__class__.__name__) + " | " + animal.get_name())
        while animal.is_hungry():
            animal.feed()
        animal.talk()

        if isinstance(animal, Dog):
            animal.fetch_stick()
        elif isinstance(animal, Cat):
            animal.chase_laser()
        elif isinstance(animal, Skunk):
            animal.stink()
        elif isinstance(animal, Unicorn):
            animal.sing()
        elif isinstance(animal, Dragon):
            animal.breath_fire()

if __name__ == "__main__":
    main()
