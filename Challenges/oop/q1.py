# Student with average grade.
class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def average(self):
        return sum(self.marks)/len(self.marks)
    
s1 = Student("Biraj", [50,67,54,56,34])
print(f"Average marks of {s1.name} is: {s1.average()}")
