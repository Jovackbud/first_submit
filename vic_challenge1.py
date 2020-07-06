h = int(input('height in inches:'))
w = int(input('weight in pounds:'))
BMI = (w * 703) / (h ** 2)
print(f'Your Body Mass Index is {BMI}')

if BMI == 30 or BMI > 30:
    print('You are Obese.')
elif BMI == 25 and BMI < 30:
    print('You are Overwight.')
elif BMI == 18.5 and BMI < 25:
    print('You are normal.')
else:
    print('You are underweight.')
