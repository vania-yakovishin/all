class Animal:
   def __init__(self, name):
    self.name = name
   def speak(self):
        return f"{self.name} щось каже"

class Dog(Animal):
   def bark(self):
        return f"{self.name} голосно гавкає"

animal = Animal("Тварина")
print(animal.speak())
dog=Dog("Собака")
print(dog.speak())
print(dog.bark())

class BreedDog(Animal):
   def _init__(self, name, breed):
      super().__init__(name)
      self.breed = breed
   def speak(self):
      return f"{super().speak()} i { self.name} є {self.breed}"
   breed_dog=BreedDog("Собака", "Дог")
   print(breed_dog.speak())

class MyClass:
    def __init__(self, value):
         self.__my_private_method(value)
    def __my_private_method(self, value):
         print(f"Private method called with value: {value}")
obj = MyClass(42)

