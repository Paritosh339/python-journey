class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def display_info(self):
        print("Student name: ", self.name)
        print("Student age: ", self.age)
        print("Student grade: ", self.grade)

student1 = Student("Paritosh" , 24 , "A" )
student1.display_info()

student2 = Student("Sunil", 23, "B")
student2.display_info()