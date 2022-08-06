#mapping
# map() can be called on any list or iterable

numbers_list = [0,1,2,3,4,5,6,7,8,9]

#in order to double each number in a list, follow below code
double_list = []

for num in numbers_list:
    double_list.append(num*2)
print(double_list)

#above is the old way. Below is using map()

#first define the basic function you want, in this case doubling, but could also be diviing, tripling, etc.

def double(x):
    return x*2

def subtract_from_list(x):
    return x-1

double_list_fucntion = list(map(double, numbers_list))
subtract_from_list = list(map(subtract_from_list, numbers_list))
print(double_list_fucntion)
print(subtract_from_list)