class Dog:
    species = 'caniche'

    def __init__(self, name, age):
        self.name = name
        self.age = age


bambi = Dog("Bambi", 5)
mikey = Dog("Rufus", 6)
blacky = Dog("Fosca", 9)
coco = Dog("Coco", 13)
perla = Dog("Neska", 3)

print("{} is {} and {} is {}.". format(bambi.name, bambi.age, mikey.name, mikey.age))

if bambi.species == "caniche":
    print("{0} is a {1}!".format(bambi.name, bambi.species))

def get_biggest_number (*argument):
    
    max=0
    for i in argument:
        if (type(i) is int) == False:
            return ("Error: Arguments must be integers")
        if i>max:
            max=i
    return (max)


print('The biggest number among the given is: ' , get_biggest_number(1 , 4 , 5 , -4 , 6 , 123 , 0))