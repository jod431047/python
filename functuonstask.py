
# Create a simple function that takes 2 numbers and print their values

def firstfunc(x=5, y=10):
    return print(f'x = {x} , y = {y}')
firstfunc(5 , 10)
                                         #x = 5 , y = 10
firstfunc(5.6 ,10)                       #x = 5.6 , y = 10

# Create a function that can take any number of arguments and print the sum of them

def mysum(s=0 ,o=0):
    return s + o
print(mysum(25,60))

# Create the same sum function using the lambda
myjihad =lambda x , y : x + y
print(myjihad(13,63))
