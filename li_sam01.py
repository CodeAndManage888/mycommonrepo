#--------------------------------------------------------------
class tester: 
  def __init__(self,id):
    self.id = str(id)
    id="224"
temp = tester(12)
print(temp.id)

#--------------------------------------------------------------
for i in range(3):
  print(i,end='')
print("")
#--------------------------------------------------------------
def f(x):
  return x + 1

print(f(f(f(2))))

#--------------------------------------------------------------
myList=[1,2,3,5,3,4,6,9]

print(myList[-6:6])
#--------------------------------------------------------------
#what is the output of following snippet?
def hello_python(func):

  def wrapped():
    return func() + " Python "

  return wrapped

def hello_decorator(func):

  def wrapped():
    return func() + " Decorator "

  return wrapped

@hello_python
@hello_decorator
def hello():
  return "Hello!"

print(hello())

#--------------------------------------------------------------
#What is the output of the below code?
def fun(n,res=1):

  if(n<=0):
     return res
  return fun(n-1,n*res)

print(fun(5))
