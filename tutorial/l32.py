class A:
    property1 = 'property1'
    property2 = 'property2'
    name='text'

    def say_hi(self, name=''):
        if name:
            return 'Hi' + name
        else:
            return 'hello' + self.name

a = A()
# a.property1 = 'property1'
# a.property2 = 'property2'
# print(a)
print(a.property1)
print(a.say_hi('Name'))

