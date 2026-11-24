class Pet:
    print("Welcome to Pet Profile!")

pet_object = Pet()

class PetProfile:
    category = "pet"

    def __init__(self,name,animal_type,age,favorite_food):
        self.name = name
        self.animal_type = animal_type
        self.age = age
        self.favorite_food = favorite_food

Sam = PetProfile("Sammy","Dog",8,"Beef jerky")
Matilda = PetProfile("Tilly","Cat",5,"Tuna")
print("Sam is a {}".format(Sam.category))
print("Matilda is a {}".format(Matilda.category))

print("The first pet's name is {}".format(Sam.name))
print("The second pet's name is {}".format(Matilda.name))

print("{} favorite food is {}".format(Sam.name, Sam.favorite_food))
print("{} favorite food is {}".format(Matilda.name, Matilda.favorite_food))

print("{}'s age is {}".format(Sam.name, Sam.age))
print("{}'s age is {}".format(Matilda.name, Matilda.age))

print("{} is a {}".format(Sam.name, Sam.animal_type))
print("{} is a {}".format(Matilda.name, Matilda.animal_type))