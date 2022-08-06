from functools import reduce

#mapping
# map() can be called on any list or iterable

numbers_list = [1,2,3,4,5,6,7,8,9]

#in order to double each number in a list, follow below code
double_list = []

for num in numbers_list:
    double_list.append(num*2)
# print(double_list)

#above is the old way. Below is using map()

#first define the basic function you want, in this case doubling, but could also be diviing, tripling, etc.

def double(x):
    return x*2

def subtract_from_list(x):
    return x-1

double_list_fucntion = list(map(double, numbers_list))
subtract_from_list = list(map(subtract_from_list, numbers_list))
# print(double_list_fucntion)
# print(subtract_from_list)


#FILTERING
#used when you want to find some specific piece of information in a list or iterable

#write a program to find if elements are even or not

def is_even(x):
    if x%2 == 0:
        return x

even_list = list(filter(is_even, numbers_list))
# print(even_list)


#Lambdas
#one line, unnamed functionas that can be defined inside larger expressions
#example: lambda x,y: x+y

double_list_with_lambda = list(map(lambda x: x*2, numbers_list))
times_5 = list(map(lambda x: x*5, numbers_list))
print(times_5)
print(double_list_with_lambda)


#list comprehensions
#reduce - take a list and reduce it down to a single value (a sum or average)

#in order for get_sum to work you need to make a function that takes the accumulated value and current value

def get_sum(acc, x):
    print(f'acc is {acc}',f'x is {x}' )
    return x + acc

def get_min(acc, x):
    return min(acc, x)

summed_list = reduce(get_sum, numbers_list)
min_value = reduce(get_min, numbers_list)
print(min_value)
# print(summed_list)

employees = [{
    'name': 'Jane',
    'salary':90000,
    'job_title': 'developer'
}, {
    'name': 'Bill',
    'salary':50000,
    'job_title': 'writer'
}, {
    'name': 'Cathy',
    'salary':120000,
    'job_title': 'executive'
}, {
    'name': 'Jeffrey',
    'salary': 48500,
    'job_title': 'product owner'
}, {
    'name': 'Steve',
    'salary': 100000,
    'job_title': 'developer'
}
]

def is_developer(employee):
    return employee['job_title'] == 'developer'

developers = list(filter(is_developer, employees))

def get_salary(employees):
    return employees['salary']
# print(developers)

developer_salaries = list(map(get_salary,developers))
print(developer_salaries)

def get_sum(acc,x):
    return acc + x

total_dev_salary = reduce(get_sum, developer_salaries)
print(total_dev_salary)

average_dev_salary = total_dev_salary/len(developer_salaries)
print(average_dev_salary)