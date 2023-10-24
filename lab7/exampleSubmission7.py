def power(x,y):
    if y == 0:
        return 1
    else:
        return x * power(x, y-1)

def cat_ears(n):
    if n == 0:
        return 0
    else:
        return 2 + cat_ears(n-1)

def alien_ears(n):
    if n <= 0:
        print('Enter a number greater than 0.')
        return

    if n == 1:
        return 3
    elif n % 2 == 0:
        return 2 + alien_ears(n-1)
    else:
        return 3 + alien_ears(n-1)
