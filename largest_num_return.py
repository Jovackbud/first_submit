num_list = []
n = 10
for i in range(0, n):
    num = int(input('Enter a number here:'))
    num_list.append(num)
num_list.sort()
print('\nthe largest of the numbers you entered is '.title() + str(num_list[-1]))
