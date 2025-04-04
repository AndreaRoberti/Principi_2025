class Person():
    def __init__(self, name, surname):
        self.name_ = name
        self.surname_ = surname
        self.age_ = 0

    def printPerson(self):
        print("-----------------")
        print(self.name_)
        print(self.surname_)
        print(self.age_)
        print("-----------------")

    def setAge(self, age):
        self.age_ = age
        print(self.age_)

##########################

# person_1 = Person("Andrea","Roberti")
# person_1.printPerson()
# person_1.setAge(34)
# person_1.printPerson()
# print(person_1.age_)

# person_2 = Person("Anna","Corbellari")
# person_2.printPerson()