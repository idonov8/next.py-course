class Cat():
    count_animals = 0

    def __init__(self, age, name="Octavio"):
        self._name = name 
        self._age = age
        Cat.count_animals += 1
    
    def birthday(self):
        self._age += 1
    
    def get_age(self):
        return self._age
    
    def set_name(self, name):
        self._name = name 

    def get_name(self):
        return self._name
def main():
    pipsi = Cat(8, "Pipsi")
    octavio = Cat(10)
    print(pipsi.get_name(), octavio.get_name())
    octavio.set_name("Octaviuuu")
    print(octavio.get_name())
    print(Cat.count_animals)

main()