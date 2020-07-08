s = 'Hello, I am Jappy-Lappy-Happy'
sa = ''
for item in s:
    if item .isalnum():
        sa += item
print(sa[::-1].lower())