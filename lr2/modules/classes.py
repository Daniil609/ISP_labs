
class Person:

    def __init__(self, name, pers):
        self.name = name
        self.pers = pers 
        
    l = lambda x, y: x * y




class Computer:

    def __init__(self, model):
        self.model = model





class User:

    name = "Jonh Smith"
    adress = "New York"

    def func(arg1, arg2):
        return arg1 + arg2

    l = lambda x, y: x + y

user = User()
comp = Computer("PC")
person2 = Person("Mike", None)
person1 = Person("Henry", person2)    




