class Student:
    def __init__(self, name, current_class, id):
        self.id = id
        self.name = name
        self.current_class = current_class


    def __repr__(self) -> str:
        return f'Student with name: {self.name}, class: {self.current_class}, id: {self.id}'



class Teacher:
    def __init__(self, id, name, subject):
        self.id = id
        self.name = name
        self.subject = subject

    def __repr__(self):
        return f'Teacher name {self.name}, id: {self.id}, subject: {self.subject}'



class School:
    def __init__(self, name):
        self.name = name
        self.teachers = []
        self.students = []

    def add_student(self, name, subject):
        id = len(self.teachers) + 101
        teacher = Teacher(id, name, subject)
        self.teachers.append(teacher)


    def enroll(self, fee, name):
        if fee < 6500:
            return 'Not enough fee'
        else: 
            id = len(self.students) + 1
            student = Student(name, 11, id)
            self.students.append(student)
            return f'{name} is enrolled with {id} ID, extra money: {fee - 6500}'
        
    
    def __repr__(self):
        print('Welcom to', self.name)
        print('--------- OUR TEACHERS ---------')

        print('--------- OUR STUDENTS ---------')
        for stu in self.students:
            print(stu)




# khan = Student('Imran', 11, 11002)
# mia = Teacher(101, 'Nah Khan', 'DSA')

# print(khan)
# print(mia)


phitron = School('Phitron')
phitron.enroll(56000, "kabir")
phitron.enroll(1200, "Naila")
phitron.enroll(5000, "Khan")

phitron.add_student('Hanid', "DS")
phitron.add_student('nia', "OK")


print(phitron)