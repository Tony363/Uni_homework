import random

#  Write a Python program to calculate the sum of a list of numbers
def sum_list(lst,total = 0):
    
    total += lst[0]
    del lst[0]
    if len(lst) == 0:
        return total
    else:
        return sum_list(lst,total)

# print(sum_list([i for i in range(11)]))

def recursion_list(lst,total = 0):
   
    if len(lst) == 0:
        return total

    elif type(lst[0]) == type([]):
        total += sum_list(lst[0])
        del lst[0]
        return recursion_list(lst,total)
    else:
        total += lst[0]
        del lst[0]
        return recursion_list(lst,total)

print(recursion_list([1, 2, [3,4], [5,6]]))
            

# Write a Python program to converting an Integer to a string in any base
def to_string(number):
    return '{}'.format(number)

print(f'i am {to_string(18)} years old')


# Write a Python program to get the factorial of a non-negative integer. 
def factorial(n,count= 1,number=1):
    number *= count
    count += 1
    if count == n+1:
        return number
    else:
        return factorial(n,count,number)

print(factorial(8))

#  Write a Python program to solve the Fibonacci sequence using recursion.
def fibonacci(n,sequence = [0,1]):
    number = sequence[-1] + sequence[-2]
    sequence.append(number)
    if len(sequence) == n:
        return sequence
    else:
        return fibonacci(n,sequence)

print(fibonacci(34))

def non_negative(lst,addition=0):
    # print(lst)
    if len(lst) == 0:
        return addition 
    elif lst[0] > 0:
        addition += lst[0]
        del lst[0]
        return non_negative(lst,addition)
    else:
        del lst[0]
        return non_negative(lst,addition)

print(non_negative([random.randrange(-1,2) for i in range(10)]))


def formula(number,subraction = 2,addition=0):
    
    if number - subraction <= 0:
        return addition + number

    elif number - subraction >= 0:
        addition += (number - subraction) 
        subraction *= 2
        return formula(number,subraction,addition)

print(formula(6))

def harmonic_sum(n,count = 1,addition = 0):
    addition += 1/count
    # print(addition)
    if count == n:
        return addition
    else:
        count += 1
        return harmonic_sum(n,count,addition)

print(harmonic_sum(6))

def geometric_sum(n,ratio,total = 1,count = 0):
    # print(total)
    if count == n:
        return total
    else:
        total = total + ratio
        ratio *= ratio
        count += 1
        return geometric_sum(n,ratio,total,count)

print(geometric_sum(3,.5))

def a_to_power_b(a,b):
    return a**b

def greatest_common_divisor(a,b):
    if(b==0): 
        return a 
    else: 
        return greatest_common_divisor(b,a%b) 
   
print(greatest_common_divisor(4,14))
    

