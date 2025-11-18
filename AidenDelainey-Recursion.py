##-_-_-_-_-_-_-_-_-_-_-_-##
## Recursion             ##
## Aiden Delainey        ##
## oct 29 / 2025         ##
##_-_-_-_-_-_-_-_-_-_-_-_##


## Functions ##
def doubler(amount, number):
    if amount == 0: #base
        print(number) #prints the number
        doubler(amount-1, number*2) #calls itself with less counts and doubles the number
       
## Main Code ##
doubler(5, 2) #input amount of times doubled and the number doubled