# Remember to import random function here

my_list = [4, 5, 734, 43, 45]

# The magic goes below
import random
for i in range(1, 11):
    my_list.append(random.randint(1,100))
    print(my_list)