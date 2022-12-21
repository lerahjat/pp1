class Student:
   
    id = 100000
    def __init__(self, name, surname,study):
            self.name = name
            self.surname = surname
            self.study = study
            self.id = Student.id
            Student.id += 1

    def __str__(self):
           return f"{self.name} \n{self.surname} \n({Student.id})\n{self.study}"

student = Student("Valeriia","Lisovska","Applied Informatics")
print(student)