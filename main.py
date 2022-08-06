# Why functional programming?
# Immutability, separating functions and data, first class functions

#below is an example of calling one fucntion with another function
# def say_hello(name):
#     print(f"Hello {name}")
# say_hello2 = say_hello
# say_hello2('Magnus')
#
# ENVIRONMENT = 'prod'
#
# def fetch_real_data():
#     print('time intensive process occuring now, please wait...')
#
# def fetch_fake_data():
#     print('Returning fake data')
#     return{
#         'name':'Jane Doe',
#         'age': 34
#     }
# fetch_data = fetch_real_data() if ENVIRONMENT == 'prod' else fetch_fake_data()
# data = fetch_data()

#below is an example of multiple functions that manipulate a number being called in one function

#add one
# def add_one(num):
#     new_number = num + 1
#     return new_number
#
# #subtract 2
# def subtract_2(num):
#     new_number = num -2
#     return new_number
#
# #times 3
# def times_3(num):
#     new_number = (num * 3)
#     return new_number

#Now I want to take my three functions and put them in a list so that I can throw them in a for loop and use all for any num

# function_list = [add_one, subtract_2, times_3]

my_num = 4
# for func in function_list:
#     my_num = func(my_num)
#     print(my_num)


#Below is an example of using a function to call other functions where the second function contains the inputs
def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def combine_5_and_9(func, x,y):
    return func(x,y)
print(combine_5_and_9(subtract, 5, 7))
print("I am testing Git")


def count_to_x(x):
    for y in range (x):
        print(y)
# def return_name(str1, str2):
#     return f'{str1} {str2}'
#
# print(return_name("Magnus", "Herweyer"))

# def create_printer():
#     def printer():
#         print("hello functional")
#     return printer()
#
# my_printer = create_printer()
# my_printer

count_to_x(10)

#
# def double(x):
#     return x*2
#
# def triple(x):
#     return x*3
#
# def quadruple(x):
#     return x*4


def create_multiplier(a):
    def multiplier(x):
        return x*a
    return multiplier

double = create_multiplier(2)
triple = create_multiplier(3)
quadruple = create_multiplier(4)

print(double(3))
print(triple(3))
print(quadruple(3))