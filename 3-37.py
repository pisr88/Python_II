import math

argument_list = [x/10 for x in range(0,1010)]


formula = input('Wprowadź działanie: ')

for x in argument_list:
    print(eval(formula))
