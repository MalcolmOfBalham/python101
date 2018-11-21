#module contains random bits and bobs for the tutorial
#file:///C:/Users/malco/tools/python-3.7.0-docs-html/python-3.7.0-docs-html/tutorial/index.html

def getFibonacciNumbers(n):
    #next fib number is the current one plus the next
    #e.g. 1, 2, 5
    a, b = 0, 1    #multi-assignment!
    result = []
    while a < n:
        result.append(a)
        a, b = b, a + b

    return result
    
def concatItems(*args, separator="|"):
    return separator.join(args)

def scope_test():
    def do_local():
        message = "local!"
    
    def do_nonlocal():
        nonlocal message
        message = "nonLocal!"
    
    def do_global():
        global message
        message = "global!"

    message = "test message"
    print(f"message value at start {message}")
    do_local()
    print(f"message value after dolocal {message}")
    do_nonlocal()
    print(f"messgae value after do_nonlocal {message}")
    do_global()
    print(f"message value after do_global {message}")
