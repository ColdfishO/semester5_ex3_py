# 3
for i in range(1, 11):
    if i == 1 or i == 10:
        for j in range(1, 11):
            print('*', end=' ')
        print('')
    else:
        print('*                 *')

print('\n')
# 4
for i in range(1, 11):
    if i == 1 or i == 10:
        for j in range(1, 11):
            if j == 10:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print('')
    else:
        print('                  *')

print('\n')
# 5
for i in range(1, 11):
        for j in range(1, 11):
            if i == j or j == 10:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print('')
print('\n')
for i in range(1, 11):
        for j in range(1, 11):
            if i == j or j == 10:
                print('*', end=' ')
            else:
                if i > 1 and j == 11 - i:
                    print('*', end=' ')
                else:
                    print(' ', end=' ')

        print('')

print('\n')
# 6
for i in range(1, 11):
    if i % 2 == 0:
        print('', end='')
    else:
        print('*', end=' ')
    for j in range(2, 11):
        if j % 2 == 0:
            print(' ', end=' ')
        else:
            print('*', end=' ')
    print('')

print('\n')
# 7
print('  ', end=' ')
for i in range(1, 11):
    if i < 10:
        print('', i, end=' ')
    else:
        print(i)
for i in range(1, 11):
    if i < 10:
        print('', i, end=' ')
    else:
        print(i, end=' ')
    for j in range(1, 11):
        if i == 3 and j < 4:
            print('', end=' ')
        elif i == 4 and j < 3:
            print('', end=' ')
        elif i == 2 and j < 5:
            print('', end=' ')
        elif i == 1 and j < 10:
            print('', end=' ')
        elif 4 < i < 10 and j == 1:
            print('', end=' ')
        print(i*j, end=' ')

    print('')

print('\n')
# 8
for i in range(1, 11):
    if i == 1:
        for j in range(1, 11):
            print('*', end=' ')
    else:
        for j in range(1, 11-(i-1)):
            print('*', end=' ')
    print('')

print('\n')

for i in range(1, 11):
    if i == 1:
        for j in range(1, 11):
            print('*', end=' ')
    else:
        for j in range(1, 11):
            if j < i:
                print(' ', end=' ')
            else:
                print('*', end=' ')
    print('')

print('\n')

for i in range(1, 11):
    if i == 10:
        for j in range(1, 11):
            print('*', end=' ')
    else:
        for j in range(10, 0, -1):
            if j > i:
                print(' ', end=' ')
            else:
                print('*', end=' ')
    print('')

print('\n')

for i in range(1, 11):
    if i == 10:
        for j in range(1, 11):
            print('*', end=' ')
    else:
        for j in range(1, (i+1)):
            print('*', end=' ')
    print('')

print('\n')
# 9
print('  ', end=' ')
for i in range(1, 11):
    if i < 10:
        print('', i, end=' ')
    else:
        print(i)
for i in range(1, 11):
    if i < 10:
        print('', i, end=' ')
    else:
        print(i, end=' ')
    for j in range(1, 11):
        if i ** j > j ** i:
            print(' >', end=' ')
        elif i ** j < j ** i:
            print(' <', end=' ')
        else:
            print(' =', end=' ')

    print('')

print('\n')
# 10
for i in range(-15, 15):
    for j in range(-15, 15):
        if (j**2 + i**2)**(1/2) <= 14:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print('')
print('\n')
for i in range(-15, 15):
    for j in range(-15, 15):
        if (j**2 + i**2)**(1/2) <= 14 and (j**2 + i**2)**(1/2) >= 13:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print('')