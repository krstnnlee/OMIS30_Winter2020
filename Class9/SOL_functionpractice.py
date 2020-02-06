# Function that takes in a value and prints out the number multiplied by 3 (inside the function)
# one input only
# no variables returned
# name it function1
def function1(x):
    y = x * 3
    print(y)

# Function that takes in a value and returns the number divided by 3
# one input
# one variable returned
# name it function2
def function2(x):
    y = x / 3
    return y


# Function that takes in two strings, finds the first character in each of those strings, and combines them
# two inputs
# one variable returned
# name it function3
def function3(x,y):
    z = x[0] + y[0]
    return z


# Function that takes in two strings, finds the first character in each of those strings, and returns both of those in order
# two inputs
# two variables returned
# name it function4
def function4(x,y):
    a = x[0]
    b = y[0]
    return a, b


# Function that two numbers, takes the sum, and returns that
# two input
# one variable returned
# use defaults for the inputs - first being 2, second being 3
# name it function5
def function5(x = 2, y = 3):
    z = x + y
    return z