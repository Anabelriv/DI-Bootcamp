from xp import Dog
import random

# train: prints the output of bark and switches the trained boolean to True

# play: takes a parameter which value is a few names of other Dog instances (use *args). The method should print the following string: “dog_names all play together”.

# do_a_trick: If the dog is trained the method should print one of the following sentences at random:
# “dog_name does a barrel roll”.
# “dog_name stands on his back legs”.
# “dog_name shakes your hand”.
# “dog_name plays dead”.

class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False

    def trained(self):
        print(f"{self.bark()} and {self.trained: True}")
        
    def play(self, *dog_names):
        print(f"{', '.join(dog_names)} all play together")
    
    def do_a_trick(self):
        if self.trained == True:
            tricks = [
                f"{self.name} does a barrel roll",
                f"{self.name} stands on his bacl legs",
                f"{self.name} shakes your hand",
                f"{self.name} plays dead"]
            print(random.choice(tricks))


    def do_a_trick(self):
        if self.trained:
            tricks = [
                f"{self.name} does a barrel roll",
                f"{self.name} stands on his back legs",
                f"{self.name} shakes your hand",
                f"{self.name} plays dead"
            ]
            

