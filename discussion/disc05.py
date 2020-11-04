class Instructor:
    degree = "PhD (Magic)"# this is a class attribute
    def __init__(self, name):
        self.name = name

    def lecture(self, topic):
        print("Today we're learning about " + topic)

dumbledore = Instructor("Dumbledore")
class Student:
    instructor = dumbledore

    def __init__(self, name, ta):
        self.name = name
        self. understanding = 0
        ta.add_student(self)

    def attend_lecture(self, topic):
        Student.instructor.lecture(topic)
        if Student.instructor == dumbledore:
            print(Student.instructor.name + " is awesome!")
        else:
            print("I miss Dumbledore.")
        self.understanding += 1

    def visit_office_hours(self, staff):
        staff.assist(self)
        print("Thanks, " + staff.name)

class TeachingAssistant:
    def __init__(self, name):
        self.name = name
        self.students = {}

    def add_student(self, student):
        self.students[student.name] = student

    def assist(self, student):
        student.understanding += 1


class Email:
    '''3 instance attributes: the message, the sender name,
    and the recipient name.
    '''
    def __init__(self, msg, sender_name, recipient_name):
        self.message = msg
        self.sender = sender_name
        self.recipient = recipient_name

class Mailman:
    '''an instance attribute clients, which is a dictionary
    that associates client names with client objects.
    '''
    def __init__(self):
        self.clients = {}

    def send(self, email):
        '''Take an email and put it in the inbox of the client
        it is addressed to.
        '''
        email.recipient.receive(email)

    def register_client(self, client, client_name):
        '''Takes a client object and client_name and adds it
        to the clients instance attribute.
        '''
        self.clients[client_name] = client

class Client:
    '''has instance attributes name(used for addressing emails to the client)
    , mailman(used to send emails to other clients), and inbox(a list of all emails
     the client has received).
     '''
    def __init__(self, mailman, name):
         self.inbox = []
         self.name = name
         self.mailman = mailman

    def compose(self, msg, recipient_name):
        '''send an email with the given message msg to the given
        recipient client.
        '''
        email = Email(msg, self.name, recipient_name)
        self.mailman.send(email)


    def receive(self, email):
        '''Take an email and add it to the inbox of this client.
        '''
        self.inbox.append(email)


class Pet(object):
    def __init__(self, name, owner):
        self.is_alive = True
        self.name = name
        self.owner = owner
    def eat(self, thing):
        print(self.name + " ate a " + str(thing) + "!")
    def talk(self):
        print(self.name)

class Dog(Pet):
    def __init__(self, name, owner):
        Pet.__init__(self, name, owner)
    def talk(self):
        print(self.name + ' says woof!')

class Cat(Pet):
    def __init__(self, name, owner, lives = 9):
        Pet.__init__(self, name, owner)
        Cat.lives = lives

    def talk(self):
        '''A cat says meow! when asked to talk.'''
        print(self.name + 'says meow!')

    def lose_life(self):
        if self.lives:
            self.lives = self.lives - 1
        if not self.lives:
            self.is_alive = False

class NoisyCat(Cat):
    '''A cat that repeats things twice.'''
    def talk(self):
        Cat.talk(self)
        Cat.talk(self)

class A:
    def f(self):
        return 2
    def g(self, obj, x):
        if x == 0:
            return A.f(obj)
        return obj.f() + self.g(self, x - 1)

class B(A):
    def f(self):
        return 4



class Yolo:
    '''
    >>> x = Yolo(1)
    >>> x.g(3)
    4
    >>> x.g(5)
    6
    >>> x.motto = 5
    >>> x.g(5)
    10
    '''
    def __init__(self, motto):
        self.motto = motto
    def g(self, x):
        return self.motto + x
