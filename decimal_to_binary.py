# This program converts decimal value to binary value with higher precision
# This program takes into consideration that fractional part should be calculated by integers due to inaccuracy
# of floating point numbers
# Author: Matin Huseynzade
# Date: 22-02-2022
# Class: CENG214
# ID: 280201086

# Parantheses indicate looping decimals e.g: 0.0(10) means 0.01010101010101010101010101010........
while True:
    decimal_value = input("Enter decimal value (e.g: 587.254): ")
    if '.' not in decimal_value:
        decimal_value = decimal_value + '.0'

    integer_part = int(decimal_value.split(".")[0])
    fractional_part = int(decimal_value.split(".")[1])
    integer_limit = 10**(len(decimal_value.split(".")[1]))

    binary_integer_part = bin(integer_part)[2:]
    stack_of_binary_digits = []
    stack_of_fractional_part = []
    is_loop = False
    loop_index = 0



    while fractional_part != 0:
        stack_of_fractional_part.append(fractional_part)
        fractional_part *= 2
        

        if fractional_part >= integer_limit:
            stack_of_binary_digits.append(1)
            fractional_part -= integer_limit
        else:
            stack_of_binary_digits.append(0)
            
        if fractional_part in stack_of_fractional_part:
            is_loop = True
            loop_index = stack_of_fractional_part.index(fractional_part)
            break
        # print(stack_of_fractional_part)
        # print(stack_of_binary_digits)



    binary_fractional_part = ''.join(str(x) for x in stack_of_binary_digits)
    if is_loop:
        binary_fractional_part = binary_fractional_part[:loop_index] + '(' + binary_fractional_part[loop_index:] + ')'

    result = binary_integer_part + '.' + binary_fractional_part


    print("Binary represenation of", decimal_value, "is", result)

