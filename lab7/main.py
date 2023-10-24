def main():
    print(alien_ears(7))
    print(alien_ears2(7))
    """
    7 = 3
    6 = 2
    5 = 3
    4 = 2
    3 = 3
    2 = 2
    1 = 3
    = 18
    """

def alien_ears(n):
    if n <= 0:
        print('Enter a number greater than 0.')
        return

    # if n == 1:
    #     return 3
    # elif n % 2 == 0:
    #     return 2 + alien_ears(n-1)
    # else:
    #     return 3 + alien_ears(n-1)

    if n % 2 == 0:
        return 2 + alien_ears(n-1)
    else:
        return 3 + alien_ears(n-1)

def alien_ears2(n):
    if n <= 0:
        print('Enter a number greater than 0.')
        return

    elif is_even(n):
        return 2 + alien_ears(n-1)
    else:
        return 3 + alien_ears(n-1)

def is_even(n):
  return n % 2 == 0

if __name__ == '__main__':
  main()
