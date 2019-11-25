Using a closure, recreate the partial() function:
- The first argument should be a function.
- The second argument should allow for any arbitrary amount of arguments.
Using the partial() function you wrote, call partial() on the add() function, and pass in 2.
- Assign the returned function to the variable add_two.
Call print() on add_two(7).

def add(a, b):
    return a + b

def partial(func, *args):
    parent_args = args
    def inner(*inner_args):
        return func(*(parent_args + inner_args))
    return inner

add_two = partial(add, 2)
print(add_two(7))
