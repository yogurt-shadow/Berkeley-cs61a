def is_sorted(n):
    '''
    >>> is_sorted(2)
    True
    >>> is_sorted(22222)
    True
    >>> is_sorted(9876543210)
    True
    >>> is_sorted(9087654321)
    False
    '''
    if n < 10:
        return True
    elif (n // 10) % 10 < n % 10:
        return False
    else:
        return is_sorted(n // 10)

def mario_number(level):
    '''
    >>> mario_number(10101)
    1
    >>> mario_number(11101)
    2
    >>> mario_number(100101)
    0
    '''
    if level < 10 or level % 10 == 0:
        return level and level % 10
    elif (level // 10) % 10 == 0:
        return mario_number(level // 100)
    else:
        return mario_number(level // 100) + mario_number(level // 10)

def make_change(n):
    '''
    >>> make_change(5)
    2
    >>> make_change(6)
    2
    '''
    if n < 1:
        return 0
    elif n >= 1 and n < 3:
        return make_change(n - 1) + 1
    elif n >= 3 and n <4:
        return min(make_change(n - 3) + 1, make_change(n - 1) + 1)
    else:
        return min(make_change(n - 4) + 1, make_change(n - 3) + 1, make_change(n -1) + 1)

def elephant(name, age, can_fly):
    '''
    >>> dumbo = elephant("Dumbo", 10, True)
    >>> elephant_name(dumbo)
    'Dumbo'
    >>> elephant_age(dumbo)
    10
    >>> elephant_can_fly(dumbo)
    True
    '''
    return [name, age, can_fly]

def elephant_name(e):
    return e[0]

def elephant_age(e):
    return e[1]

def elephant_can_fly(e):
    return e[2]

def elephant_roster(elephants):
    return [elephant_name(e) for e in elephants]

def elephant(name,age,can_fly):
    return [[name, age], can_fly]

def elephant_name(e):
    return e[0][0]

def elephant_age(e):
    return e[0][1]

def elephant_can_fly(e):
    return e[1]

def elephant(name, age, can_fly):
    '''
    >>> chris = elephant("Chris Martin", 38, False)
    >>> elephant_name(chris)
    'Chris Martin'
    >>> elephant_age(chris)
    38
    >>> elephant_can_fly(chris)
    False
    '''
    def select(command):
        if command == "name":
            return name
        if command == "age":
            return age
        if command == "can_fly":
            return can_fly
    return select

def elephant_name(e):
    return e("name")
def elephant_age(e):
    return e("age")
def elephant_can_fly(e):
    return e("can_fly")
