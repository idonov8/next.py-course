class Cat():
    def __init__(self, name, age):
        self.name = name 
        self.age = age
    
    def birthday(self):
        self.age += 1
    
    def get_age(self):
        return self.age
def main():
    pipsi = Cat("Pipsi", 8)
    petel = Cat("Petel", 10)
    pipsi.birthday()
    print(pipsi.get_age(), petel.get_age())

main()