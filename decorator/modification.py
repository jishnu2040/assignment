def my_decorator(func):
    def wrapper(*args, **kwargs):  # Accept any number of arguments
        print("Wrapper starts")
        print(f"Arguments passed: args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)  # Call the original function with all arguments
        print("Wrapper ends")
        return result  # Return the result from the original function
    return wrapper

@my_decorator
def add(a, b):
    return a + b

@my_decorator
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

# Call the decorated functions
sum_result = add(5, 10)
print(f"Sum result: {sum_result}")

greet("Alice")
greet("Bob", greeting="Hi")
