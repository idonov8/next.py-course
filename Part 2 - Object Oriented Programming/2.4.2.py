class BigThing():
    def __init__(self, thing):
        self._thing = thing

    def size(self):
        return self._thing if isinstance(self._thing, int) else len(self._thing)

my_thing = BigThing("balloon")
print(my_thing.size())

class BigCat(BigThing):
    def __init__(self, thing, weight):
        BigThing.__init__(self, thing)
        self._weight = weight
    
    def size(self):
        if self._weight > 20:
            return "Very Fat"
        elif self._weight > 15:
            return "Fat"
        else:
            return "OK"

cutie = BigCat("mitzy", 22)
print(cutie.size())