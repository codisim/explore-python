class Student:
    def __init__(self, name, current_class, id):
        self.id = id
        self.name = name
        self.current_class = current_class


    def __repr__(self) -> str:
        return f'Student with name: {self.name}, class: {self.current_class}, id: {self.id}'






khan = Student('Imran', 11, 11002)
mia = Teacher(101, 'Nah Khan', 'DSA')

print(khan)
print(mia)