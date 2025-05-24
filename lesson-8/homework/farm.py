class Animal:
    def __init__(self, age, name, weight, is_hungry=True, is_sleeping=True):
        self.age = age
        self.name = name
        self.weight = weight 
        self.is_hungry = is_hungry
        self.is_sleeping = is_sleeping

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Weight: {self.weight}"

    def sleep(self):
        if not self.is_sleeping:
            print(f"{self.name} is going to sleep.")
            self.is_sleeping = True
        else:
            print(f"{self.name} is already sleeping.")

    def eat(self):
        if self.is_hungry:
            print(f"{self.name} is eating.")
            self.is_hungry = False
        else:
            print(f"{self.name} is not hungry.")

    def make_sound(self):
        raise NotImplementedError("Each animal should implement its own sound.")

class Horse(Animal):
    def __init__(self, age, name, weight):
        super().__init__(age, name, weight)

    def make_sound(self):
        print(f"{self.name} says: Neigh!")

    def jump(self):
        print(f"{self.name} jumps over the fence!")

class Cow(Animal):
    def __init__(self, age, name, weight):
        super().__init__(age, name, weight)

    def make_sound(self):
        print(f"{self.name} says: Moo!")

    def produce_milk(self):
        print(f"{self.name} produces milk!")

class Sheep(Animal):
    def __init__(self, age, name, weight):
        super().__init__(age, name, weight)
    def make_sound(self):
        print(f"{self.name} says: Baa!")
    def produce_wool(self):
        print(f"{self.name} produces wool!")

bella = Horse(3, "Bella", 400)
bella.eat()
bella.sleep()
bella.jump()
bella.make_sound()
print(bella)

daisy = Cow(5, "Daisy", 500)
daisy.produce_milk()
daisy.make_sound()
print(daisy)

dolly = Sheep(2, "Dolly", 150)
dolly.produce_wool()
dolly.make_sound()
print(dolly)
