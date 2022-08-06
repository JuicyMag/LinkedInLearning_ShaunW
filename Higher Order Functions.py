#The example I'm about to write is a divison function that divides x/y but we want to check that y does not equal 0

def divide (x,y):
    #check to see if y = 0, if so warning
    # if y == 0:
    #     print("Y is 0, cannot divide by 0")
    #     return
    return x/y

#Single responcibility issue here - this function should not do 2 different things. Lets look to make this more simple.

# In this function I want to check that y does not equal 0, and then call that helped function

def check_if_y_zero(func):
    def safe_version(*args):
        if args[1] == 0:
            print("Y is 0, cannot divide by 0")
            return
        return func(*args)
    return safe_version

divide_safely = check_if_y_zero(divide)
print(divide_safely(5,0))






