def hello():
    return 'some text'

def super_func(func):
    print('Some text')
    print(func())

super_func(hello)

def some():
    return 'some text'

test = some
print(test())


def my_decorator(func):
    def func_wrapper():
        print('Before')
        func()
        print('After')
    return func_wrapper

@my_decorator
def func_test():
    print('test')

test = my_decorator(func_test)
test()
func_test()

def make_title(fn):
    def wrapper():
        title = fn()
        title = title.capitalize()
        title = title.replace(',', '')
        return title
    return wrapper

@make_title
def hi():
    return 'hello, world'

print(hi())











