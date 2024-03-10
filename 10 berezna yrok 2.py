def iter_numbers():
   for i in range(10):
       yield i
iterator = iter_numbers()
for i in iterator:
    print(i)

def func_gen():
    g = 1
    while True:
        yield g
        g += 1
d = func_gen()
print(next(d))
print(next(d))

def func_gen():
    v = 0
    while True:
     yield v
     v += 1
f = func_gen()
print(f)

f= (i for i in range(50))
print(f)
print(next(f))
print(next(f))
print(next(f))

def test_range():
    for i in range(0,1):
        yield i
i=test_range()
print(next(i))

def outer_function():
  x = 10
  def inner_function():
    nonlocal x
    x += 1
    return x
  return inner_function
function=outer_function()
print(function())

def guard_zero (operate):
   def inner (x, y):
      if y == 0:
         print("Cannot divide by 0.")
         return
      return operate(x, y)
   return inner
@guard_zero
def divide (x, y):
   return x/y

print(divide( 5,0))