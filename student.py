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



khan = Student('Imran', 11, 11002)
mia = Teacher(101, 'Nah Khan', 'DSA')

print(khan)
print(mia)