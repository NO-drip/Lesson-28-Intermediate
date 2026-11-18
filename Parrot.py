class Parrot:

    species = "Bird"
    
    def __init__(self,name,age):
        self.name = name
        self.age =  age

object_1 = Parrot("Alex", 20)
object_2 = Parrot("Frank", 10)

print("Frank is a {}".format(object_2.species))
print("Alex is suprisingly also a {}".format(object_1.species))

print("{} is {} years old".format(object_1.name,object_1.age))
print("{} is {} years old".format(object_2.name,object_2.age))