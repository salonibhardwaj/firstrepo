#fix the problems with each of these classes (1-3)

#1
class MyClass():
        def __init__(self, a , b):
            self.a = a
            self.b = b
            self.x = a + b
my_instance = MyClass(10, 20)
my_instance.x



#2
class MyClass():
    def __init__(self):
        a = 10
        b = 20
        self.x = a + b
my_instance = MyClass()
my_instance.x

#3
class MyClass():
    def __init__(self, a, b):
        self.x = a + b
my_instance = MyClass(10, 20)
my_instance.x

#4 A Fibonacci sequence is a list of values where each is the sum of the previous
#  two, e.g. [0, 1, 1, 2, 3].
#      - First write a function that takes in a list of any two values, then
#        calculates the rest of the sequence starting from that point.  It
#        should have two arguments; the starting list, and the number to
#        calculate.



def fibo(vals, n):
    for _ in range(n):
        new_val=sum(vals[-2:])
        vals.append(new_val)
    return vals

fibo([0,1],10)


#      - Second, turn this into a class that takes the same list at start,
#        but has a method that takes N as an argument and then calculates
#        the sequence.
#  Note that technically the Fibonacci sequence starts at 0, but for our
#  coding practice we can calculate it from any two starting values.

class fiboclass():
    def _init_(self,vals):
        self.vals=vals
        
        def fibo(self, n):
            fib_vals=self.vals
            for _ in range(n):
                new_val= sum(fib_vals[-2:])
                fib_vals.append(new_val)
                
            return fib_vals
            
        
        
        