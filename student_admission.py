class Student:

    college_name = "MRIT College"

    # Constructor
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    @classmethod
    def change_college(cls, new_name):
        cls.college_name = new_name

    @staticmethod
    def is_pass(marks):
        if marks >= 35:
            return "Pass"
        else:
            return "Fail"

    def display(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("College:", Student.college_name)
        print("--------------------")


s1 = Student("Aishwarya", 101)
s2 = Student("Hampana", 102)

s1.display()
s2.display()

Student.change_college("MIT College")

print("After Changing College Name\n")

s1.display()
s2.display()

result1 = Student.is_pass(80)
result2 = Student.is_pass(90)

print("Marks 80:", result1)
print("Marks 90:", result2)