class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __repr__(self):
        return f"The person's name is {self.name} and they are {self.age} years old."


print(Person('Bobsies', 77))

if __name__  == '___main__':
    print()