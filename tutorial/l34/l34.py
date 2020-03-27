from classes import Person

person1 = Person('Text')
person1.print_info()

person2 = Person('Some')
# print(person2.__age)
# print(person2._Person__age)
person2.print_info()
# print(person2.get_age())
# person2.set_age(40)
print(person2.age())

person2.age = 35