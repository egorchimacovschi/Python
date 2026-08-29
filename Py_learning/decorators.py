#Decorator = a funciton that extends the behaviour of another funciton
#            w/o modifying the base function
#            Pass the base function as an argument to the decorator

def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("You add sprinkles")
        func(*args, **kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("You add funge")
        func(*args, **kwargs)
    return wrapper

@add_fudge
@add_sprinkles
def get_ice_cream(type):
    print(f"Here is youre ice cream with {type}")

get_ice_cream("vanilla")

