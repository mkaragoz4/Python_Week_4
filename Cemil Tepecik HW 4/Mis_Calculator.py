def addition (a,b):
    condition = True
    import sys
    try:
        c = float(a)
        d = float(b)
        result_a=c+d
    except:
        return print('There is a problem in your entry:', sys.exc_info()[0])
        condition = False
    while condition:
        from math import ceil
        result = ceil(result_a)  # ceil the result upper number
        return result

def substraction (a,b):
    condition = True
    import sys
    try:
        c = float(a)
        d = float(b)
        result_a=c-d
    except:
        return print('There is a problem in your entry:', sys.exc_info()[0])
        condition = False
    while condition:
        from math import ceil
        result = ceil(result_a)  # ceil the result upper number
        return result

def division (a,b):
    condition=True
    import sys
    try:
        c = float(a)
        d = float(b)
        result_a=c/d
    except:
        return print('There is a problem in your entry:',sys.exc_info()[0])
        condition=False
    while condition:
        from math import ceil
        result=ceil(result_a) #ceil the result upper number
        return result


def multiplication (a,b):
    condition = True
    import sys
    try:
        c = float(a)
        d = float(b)
        result_a=c*d
    except:
        return print('There is a problem in your entry:', sys.exc_info()[0])
        condition = False
    while condition:
        from math import ceil
        result = ceil(result_a)  # ceil the result upper number
        return result

