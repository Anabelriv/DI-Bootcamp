# class AnimalBird:
#     #class variable
#     population = 10000
    
#     @classmethod #class method = class function
#     def voice(cls): #cls = class
#         print("AAA")
 
# #instances
# dog = AnimalBird()

# print(type(dog))
# print(dog.population)

class Animal:
    def __init__(self, legs, name= 'Animal'): #initialization 
        self.name = name #self - reference to the obj
        self.legs = legs

    def voice(self):
        print(f"{self.name} is doing a voice")

    def jump(self):
        if self.legs == 0:
            print(f"{self.name} cannot jump!")
        else:
            print(f"{self.name} jumps with {self.legs} legs")
obj1 = Animal(legs = 4, name='Dog')
print(obj1.name)
obj1.voice()
zebra = Animal(legs = 4, name='Zebra')
print(zebra.name)

zebra.voice()
obj3 = Animal(legs = 0, name = "Snake")
print(obj3)


# Type_hints
def bla(some_str: str, some_tuple: tuple, number: int):
    str_capitalized = some_str.capitalize()

def add_func(num1: int, num2:int) -> int:
    return num1 + num2

def fun(a:int = 0)-> None:
    pass

def create_list_numbers()-> list[int]:
    return [1,2,3]

def create_dict_numbers() ->dict[str,int]:
    return {'A':1}

#lambda functions
# can't debug them - one liner functions
# if long - unreadable

num1 = 2 
multiply_by_two = lambda num: num*2 #accepts a number and returns a result
print(multiply_by_two(num1))

a_list = [n for n in range(100)]

b_list = list(map(multiply_by_two, a_list))

print(b_list)

c_list = list(filter(lambda num: True if num %2 ==0 else False))