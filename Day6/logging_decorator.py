def logging_decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

def say_hello():
    print("Hello")    
def say_goodbye():
    print("GoodBye")   
def say_welcome():
    print("Welcome")       
