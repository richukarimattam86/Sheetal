
import sys
from math import factorial
from pprint import  pprint as pp

""" Best practices for python """

# EAFP(It's easier to Ask Forgiveness than Permission) over LBYL(Look Before You Leap)

def process_file(path):
    print('Implement the code here')

def call_file_procession(p):
    """ NB: We are not checking for path validation or file validation of any sort
    Take a leap of faith if it fails ask for forgiveness
    """
    try:
        process_file(p)
    except OSError as e:
        print('Exception caused {0}'.format(str(e)))


""" Comprehensions """

# List comprehensions returns List
print('**********************')
words = 'My name is sheetal'.split()
print(words)
print([len(single_word) for single_word in words])
print([len(str(factorial(x))) for x in range(20)])


#Set comprehensions returns set
print('**********************')
print({len(str(factorial(x))) for x in range(20)})

#Dictionary
print('**********************')
print({word[0]:word for word in words if len(word)>2})
country_capital = {'India':'Delhi' , 'USA':'Washington DC'}
capital_country = {capital:country for country,capital in country_capital.items()}
print(pp(capital_country))


""" Iterators """
print('**********************')
iterator = iter(words)
print([next(iterator) for index in range(len(words)) ])

""" Generators"""
# Generators are single use objects
print('**********************')
def gennumbers():
    yield 1
    yield 2
    yield 3
gen_iterable = gennumbers()
print({v for v in gen_iterable})

def distinct(iterable):

    seen = set()
    for x in iterable:
        if x in seen:
            continue
        yield x
        seen.add(x)


def take(count , iterable):

    counter = 0
    for x in iterable:
        if counter == count:
            return
        counter += 1
        yield  x



def run_distinct():
    arr = [3 , 4 , 5, 9 ,9, 1]
    for item in distinct(arr):
        print(item)


def run_pipeline():
    arr = [3 , 3 , 5, 1 ,0, 1]
    for item in take(3, distinct(arr)):
        print(item)

print('**********************')
if __name__  == '__main__':
    run_pipeline()



# if __name__  == '__main__':
#     run_distinct()

""" Some important Constructors (zip, list , sum , min , max , all , any )"""


"""  Classes  """
from flight import *

print('**********************')
flight = Flight('SN060', BritishAir("GHD111", "BrtishAir 3199", 23, 6))
print(flight.flightname())
print(flight.flight_code())
print("Aircraft Registration '{}'".format(flight.aircraft_registration()))
pp(flight.seating)


