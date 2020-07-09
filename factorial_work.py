b = [x for x in range(20, 0, -1)]
print(b)
e = int(input('Enter a number between 0-21:'))

if e in b:
    if e == b[0]:
        x = e * b[1] * b[2] * b[3] * b[4] * b[5] * b[6] * b[7] * b[8] * b[9] * b[-10] * b[11] * b[12] \
            * b[13] * b[14] * b[15] * b[16] * b[17] * b[18] * b[19]
        print(x)
    elif e == b[1]:
        x = e * b[2] * b[3] * b[4] * b[5] * b[6] * b[7] * b[8] * b[9] * b[-10] * b[11] * b[12] \
            * b[13] * b[14] * b[15] * b[16] * b[17] * b[18] * b[19]
        print(x)
    elif e == b[2]:
        x = e * b[3] * b[4] * b[5] * b[6] * b[7] * b[8] * b[9] * b[-10] * b[11] * b[12] \
            * b[13] * b[14] * b[15] * b[16] * b[17] * b[18] * b[19]
        print(x)
    elif e == b[3]:
        x = e * b[4] * b[5] * b[6] * b[7] * b[8] * b[9] * b[-10] * b[11] * b[12] \
            * b[13] * b[14] * b[15] * b[16] * b[17] * b[18] * b[19]
        print(x)
    elif e == b[4]:
        x = e * b[5] * b[6] * b[7] * b[8] * b[9] * b[-10] * b[11] * b[12] \
            * b[13] * b[14] * b[15] * b[16] * b[17] * b[18] * b[19]
        print(x)
    elif e == b[5]:
        x = e * b[6] * b[7] * b[8] * b[9] * b[-10] * b[11] * b[12] \
            * b[13] * b[14] * b[15] * b[16] * b[17] * b[18] * b[19]
        print(x)
    elif e == b[6]:
        x = e * b[7] * b[8] * b[9] * b[-10] * b[11] * b[12] \
            * b[13] * b[14] * b[15] * b[16] * b[17] * b[18] * b[19]
        print(x)
    elif e == b[7]:
        x = e * b[8] * b[9] * b[-10] * b[11] * b[12] \
            * b[13] * b[14] * b[15] * b[16] * b[17] * b[18] * b[19]
        print(x)
    elif e == b[8]:
        x = e * b[9] * b[-10] * b[11] * b[12] \
            * b[13] * b[14] * b[15] * b[16] * b[17] * b[18] * b[19]
        print(x)
    elif e == b[10]:
        x = e * b[11] * b[12] \
            * b[13] * b[14] * b[15] * b[16] * b[17] * b[18] * b[19]
        print(x)
    elif e == b[11]:
        x = e * b[12] * b[13] * b[14] * b[15] * b[16] * b[17] * b[18] * b[19]
        print(x)
    elif e == b[12]:
        x = e * b[13] * b[14] * b[15] * b[16] * b[17] * b[18] * b[19]
        print(x)
    elif e == b[13]:
        x = e * b[14] * b[15] * b[16] * b[17] * b[18] * b[19]
        print(x)
    elif e == b[14]:
        x = e * b[15] * b[16] * b[17] * b[18] * b[19]
        print(x)
    elif e == b[15]:
        x = e * b[16] * b[17] * b[18] * b[19]
        print(x)
    elif e == b[16]:
        x = e * b[17] * b[18] * b[19]
        print(x)
    elif e == b[17]:
        x = e * b[18] * b[19]
        print(x)
    elif e == b[18]:
        x = e * b[19]
    else:
        x = e
        print(x)
