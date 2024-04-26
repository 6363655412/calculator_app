def do_addition(a,b):
    return a+b
def do_sub(a,b):
    return a-b
def do_div(a,b):
    try:
        return a/b
    except ZeroDivisionError as e:
        return "cannot division zero"
