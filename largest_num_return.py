num_list = []
n = 10
for i in range(0, n):
    num = int(input('Enter a number here:'))
    num_list.append(num)
num_list.sort()
print('\n\tthe largest of the numbers you entered is '.title() + str(num_list[-1]))
print('\n\tthe next largest of the numbers you entered is '.title() + str(num_list[-2]))
