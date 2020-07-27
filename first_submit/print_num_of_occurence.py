numbers = []
n = 0
while n < 7:
    new = int(input('Enter a number here:'))
    numbers.append(new)
    n += 1
print(numbers)
for num in numbers:
    a = num
    b = numbers.count(num)
    print('The number {} appeared {} time(s)'.format(a, b))
