from person import Person
import numpy as np

class Student(Person):
    def __init__(self, name , surname, id):
        super().__init__(name, surname)
        self.id_ = id

    def printStudent(self):
        self.setAge(34)
        self.printPerson()
        print(self.id_)

######################

student_1 = Student("Andrea","Roberti",1234)
student_1.printStudent()

 