# Without decorator
def add(a, b):
  return a + b

def logger(func):
  def inner(*args):
    print(f'The parent function is {func.__name__}')
    print(f'The arguments passed are {args}')
    return func(*args)
  return inner

logger_add = logger(add)
print(f'without decorator: {logger_add(2,3)}')
print()

# With decorator
@logger
def add(a, b):
  return a + b

print(f'with decorator: {add(2,3)}')
