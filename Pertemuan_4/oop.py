import datetime

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def say_my_name(self):
    print('Hello my name is ' + self.name)

p1 = Person("John", 36)

class Mathematic:
  def add(self, a, b):
    return a + b
  def substraction(self, a, b):
    return a - b
  def multiply(self, a, b):
    return a * b
  
math = Mathematic()
print(math.add + (45,2))
print(datetime.datetime.now())