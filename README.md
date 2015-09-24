# matcher
A haskell like pattern matching for python 3.


## Equality matching
You can match everything that defines a `__eq__` function:


    from matcher import Match
    
    
    @Match
    def func(a, b: 5):
        print("b is 5 here")
        
    
    @Match
    def func(a: 5, b):
        print("a is 5 here")
         
    
    @Match
    def func(a, b):
        print("a and b are not 5 here")


## Expression matching

You can also match against expressions, that evaluate to a truthy value. In these expressions all parameters are set to their actual value at runtime:


    @Match
    def multi_var_expr_func(a: 'a > b', b):
        print("a is bigger than b")


    @Match
    def multi_var_expr_func(a: 'a <= b', b):
        print("b is bigger than or equal to a")


## Order of matching

The matches are evaluated in the order they appear in the file and the first match is called. So given the little program above the following would happend:


    >>> func(5, 3)
    a is 5 here
    
    >>> func(5, 5)
    b is 5 here
    
    >>> func(1, 2)
    a and b are not 5 here
    
  
