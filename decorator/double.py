def double_result(func):
    def wrapper( *args, **kwargs):
        result = func(*args, **kwargs)
        return result *2
    return wrapper



@double_result
def add(a, b): 
    return a +b


@double_result
def squre(a):
    return a* a


addition = add(10, 24)
print(f'this is output value doubled {addition}')


double_squre = squre(10)
print(f'this is output value doubled {double_squre}')