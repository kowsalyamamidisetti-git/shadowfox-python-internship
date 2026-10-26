```python
# ShadowFox Internship - Task 1
# Python Fundamentals

# 1. Variables
print("\n--- 1. Variables ---")
name = "Kowsalya"
age = 21
print("Name:", name)
print("Age:", age)


# 2. Numbers and Arithmetic Operations
print("\n--- 2. Numbers ---")
a = 10
b = 5
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)


# 3. If-Else Conditions
print("\n--- 3. If-Else ---")
number = 10

if number > 0:
    print("The number is positive.")
else:
    print("The number is not positive.")


# 4. For Loop
print("\n--- 4. For Loop ---")
for i in range(1, 6):
    print(i)


# 5. Lists
print("\n--- 5. Lists ---")
fruits = ["Apple", "Banana", "Mango"]
print("Fruits:", fruits)

for fruit in fruits:
    print(fruit)


# 6. Dictionaries
print("\n--- 6. Dictionary ---")
student = {
    "name": "Kowsalya",
    "course": "B.Tech AIML",
    "year": "Final Year"
}

print("Student Details:", student)
print("Name:", student["name"])
print("Course:", student["course"])


# 7. File Handling
print("\n--- 7. File Handling ---")

with open("student.txt", "w") as file:
    file.write("Welcome to Python File Handling!")

with open("student.txt", "r") as file:
    content = file.read()
    print(content)


# 8. Classes and Objects
print("\n--- 8. Classes and Objects ---")

class Student:
    def __init__(self, name, course):
        self.name = name
        self.course = course

    def display(self):
        print("Student Name:", self.name)
        print("Course:", self.course)


student1 = Student("Kowsalya", "B.Tech AIML")
student1.display()


# 9. Inheritance
print("\n--- 9. Inheritance ---")

class Animal:
    def sound(self):
        print("Animals make sounds.")


class Dog(Animal):
    def bark(self):
        print("Dog barks.")


dog1 = Dog()
dog1.sound()
dog1.bark()
