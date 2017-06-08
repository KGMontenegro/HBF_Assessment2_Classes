"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

2. What is a class?

3. What is an instance attribute?

4. What is a method?

5. What is an instance in object orientation?

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.


"""

# Answers:
# 1. Polymorphism. Flexible of types without conditionals. This means that we can
# process objects in different ways based on their data type. It is like designing a 
# generic method to be applied to classes.
# Encapsulation. Don't nee to know info a method uses internally.  Bindng the data with the code. 
# Abstraction. Easy to make different, interchangeable types of whatever we are creating. 

# 2. A class is the type of things, like lists, tuples. It is a method to create things
# in a general way. 

# 3. An instance attribute is or are the values that an instance could have in order to
# define or describe the thing. If we create a class for fruits, an instance are the dif. 
# types of fruit likeL mango, banana, apple. Instance attribute is a characteristic specific
# for an instance, like color. 

# 4. Method are like functions defined on a class. 

# 5. Instance in object orientation is an individual ocurrence in a class. An instance
# of the class fruits, it could be  mango. 

# A class attribute apply to all the instances when they don't have a specific one defined. 
# for example, a class fruit an instance attribute could be color, since each fruit
# has their own color. A class attribute could be category with the value Food. All 
# instances could apply this category, that is why it is better to define it as a class
# class attribute.  

# Parts 2 through 5:
# Create your classes and class methods

# Part 2

class Student(object):
    """ 
    """
    def __init__(self, first_name, last_name, address):
        """ Initialize students info """

        self.first_name = first_name
        self.last_name = last_name
        self.address = address


std1 = Student('Jasmine', 'Debugger', '0101 Computer Street')
std2 = Student('Jacqui', 'Console', '888 Binary Ave')
print "First Name      Last_name     Address "
print "_______________________________________________________"
print  std1.first_name, "       " , std1.last_name, "     " , std1.address
print "_______________________________________________________"
print  std2.first_name, "       " , std2.last_name, "     " , std2.address
print "_______________________________________________________"

class Question(object):
    """
    """

    def __init__(self, question, answer= 'None'):
        """ Store question and its answer """
       
        self.question = question
        self.answer = answer

    def ask_and_evaluate(self):
     
        self.ans = raw_input('True or False? ')
        if self.ans == 'True':
            print True
        else:
            print False

q1 = Question("What is the capital of Alberta?", "Edmonton")
q2 = Question("Who is the author of Python?", "Guido Van Rossum")         

print "Question                         correct answer"
print "_______________________________________________________"
print q1.question, "    " , q1.answer 
print "_______________________________________________________"
print q2.question, "    " , q2.answer 
print "_______________________________________________________"


class Exam(object):
    """ 
    """

    def __init__(self, name):

        self.questions = []
        self.name = name

    def add_question(self, quest):

       self.questions.append(quest)

    def administer(self, question):

        self.questions.append(question)
        print self.question
        

class StudentExam(Student,Question):

    def __init__ (self, first_name, last_name, address):

        super(StudentExam,self)__init__(first_name, last_name, address)

    def take_test (self, question, answer, score):

        super(StudentExam,self)__init__(question, answer)
        self.score = score


def example():

    exam_ex = Exam('Midterm')
    quest_ex = exam.Question('What is the capital of Nicaragua', 'Managua')
    exam.Question('in which continent is Nicaragua', 'America')
    stu_ex = Student('Maria', 'Perez', '101 Calle Principal')



ex1 = Exam('Midterm') 
ex1.add_question('alberta_capital')
ex1.add_question('python_author')
ex2 = Exam('Final')
#q = (ex2.questions.append('ubermelon_competitor'))  
ubermelon_competitor = Question(ex2)
#ex2.questions.append('ballonicorn_color')
ballonicorn_color = Question(ex2)


print 'name     questions '
print "--------------------------------------------------"
print ex1.name, "   ", ex1.questions
print "--------------------------------------------------"
print ex2.name, "   ",  'ubermelon_competitor, ', 'ballonicorn_color'
print "--------------------------------------------------"


set_q = Question('What is the method for adding an element to a set?','.add()')
exam = Exam('midterm')
exam.add_question(set_q)
print set_q.question, set_q.answer
set_q.ask_and_evaluate()

exam = Exam('midterm')
set_q = Question('What is the method for adding an element to a set?','.add()')
exam.add_question(set_q)
pwd_q = Question('What does pwd stand for?', 'print working directory')
exam.add_question(pwd_q)
list_q = Question('Python lists are mutable, iterable, and what?', 'ordered')
exam.add_question(list_q)
#print exam.administer(set_q), exam.administer(pwd_q), exam.administer(list_q)


