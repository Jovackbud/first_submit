num = int(input('Enter a number: '))
factorial = 1

for i in range(num, 1, -1):
    factorial *= i

print('The factorial of {} is {}'.format(num, factorial))
