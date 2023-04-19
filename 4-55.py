def double(x):
    return 2 *x
 
def square(x):
    return x**2
 
def negative(x):
    return -x
 
def div2(x):
    return x/2

def generate_values(f, x_table):
    return [f(n) for n in x_table]
        
        

x_table = list(range(11))
 
print(generate_values(double, x_table))
print(generate_values(square, x_table))
print(generate_values(negative, x_table))
print(generate_values(div2, x_table))


def generate_values2(how, x_table):
 
    value_list = []
    
    for x in x_table:
        value_list.append(how(x))
 
    return value_list
 
 
print(generate_values2(double, x_table))
print(generate_values2(square, x_table))
print(generate_values2(negative, x_table))
print(generate_values2(div2, x_table))