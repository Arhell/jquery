from classes import Person, Employee

person = Person('name', 30)
print(person.age)
person.age = 35

employee = Employee("Text", 30, "Com")
employee.print_info()
employee.more_info()