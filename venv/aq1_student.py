class Student:
    name = ""
    rollNo = 0
    age = 0
    marks = 0

    def __init__(self, name = "" , rollNo = 0):
        self.name = name
        self.rollNo = rollNo

    def SetAge_(self,age):
        self.age = age

    def SetMarks_(self,marks):
        self.marks = marks

    def Display_(self):
        print("Name :{}\nRoll No :{}\nAge = {}\nMarks :{}\n".format(self.name,self.rollNo,self.age,self.marks))

#creating an object of Student
s = Student("John Ryan",125)

#diaplay initial data
s.Display_()

#setting age
s.SetAge_(23)

#setting marks
s.SetMarks_(600)

#display all the data
s.Display_()
