def My_decorator(func):
    def _my_decorator():
        print ("inside dectortar : before")
        func()
        print ("inside dectortar : after")
    return _my_decorator

@My_decorator
def my_function():
    print("Inside function")
    
    
my_function()
