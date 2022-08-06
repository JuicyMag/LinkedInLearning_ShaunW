#The example I'm about to write is a divison function that divides x/y but we want to check that y does not equal 0

def divide (x,y):
    #check to see if y = 0, if so warning
    # if y == 0:
    #     print("Y is 0, cannot divide by 0")
    #     return
    return x/y

#Single responcibility issue here - this function should not do 2 different things. Lets look to make this more simple.

# In this function I want to check that y does not equal 0, and then call that helped function

# def check_if_y_zero(func):
#     def safe_version(*args):
#         if args[1] == 0:
#             print("Y is 0, cannot divide by 0")
#             return
#         return func(*args)
#     return safe_version
#
# divide_safely = check_if_y_zero(divide)
# print(divide_safely(5,0))


#duplicatively work here - I'm doing the same function again but down here for practice

#GOAL: to call a divide() fucntion inside of a divbide by 0 check function


def check_for_zero(func):
    #checking ALL args for the
    def number_condom(*args):
        if args[1] == 0:
            print("What the fuck do you think you're doing bringing that weak shit in here? You know you can't dividie by 0 baby!")
            return
        return func(*args)
    return number_condom

std_free_division = check_for_zero(divide)

print(std_free_division(5,30))
print(std_free_division(5,0))





