a = 239.99
b = 129.75
c = 99.95
d = 350.89
a_sold = int(input('How many of a was sold:')) * a
b_sold = int(input('How many of b was sold:')) * b
c_sold = int(input('How many of c was sold:')) * c
d_sold = int(input('How many of d was sold:')) * d
commission = 200 + (0.09 * (a_sold + b_sold + c_sold + d_sold))
print(commission)
