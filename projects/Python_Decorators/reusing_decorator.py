def do_twice(func):
    def wrapper_do_twice(*args,**kwargs):
        func(*args,**kwargs)
        func(*args,**kwargs)
    return wrapper_do_twice

@do_twice
def say_whee():
    print("Whee!")

@do_twice
def greet(name):
    print(f"Hello {name}")

say_whee()
greet("World")