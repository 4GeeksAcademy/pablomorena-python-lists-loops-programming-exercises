my_list = [4,5,734,43,45,100,4,56,23,67,23,58,45]

# Your code here
def sum_odds(list):
    suma_imp = 0
    for number in list:
        if number % 2 !=0:
            suma_imp += number
    return suma_imp

sum_odds(my_list)