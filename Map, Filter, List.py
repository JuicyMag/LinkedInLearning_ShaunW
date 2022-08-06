#mapping
# map() can be called on any list or iterable

numbers_list = [0,1,2,3,4,5,6,7,8,9]

#in order to double each number in a list, follow below code
double_list = []

for num in numbers_list:
    double_list.append(num*2)
print(double_list)

#above is the old way. Below is using map()