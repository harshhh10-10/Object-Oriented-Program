class student:
    grade=12
    name="Harsh"
    def introduction(self):
        print("I am a student")
    
    def details(self):
        print("My name is",self.name)
        print("My grade is",self.grade)

obj1 = student()
obj1.introduction()
obj1.details()
