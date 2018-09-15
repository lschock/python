#my_tuple = (1, 2, 3, 4)

# def multiply(*my_tuple):
#     value = 1
#     for numeric in my_tuple:
#         value *= numeric
#     return value



def multiply(*args):
    product = 1
    for arg in args:
        product *= arg
    return product

multiply(50)
