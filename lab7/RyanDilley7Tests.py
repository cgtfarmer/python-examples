import inspect

def main():
  print('[main] START')

  runTests()

  print('[main] END')

def runTests():
  print('[runTests] START')

  power_test1()
  power_test2()
  power_test3()
  power_test4()

  catEars_test1()
  catEars_test2()
  catEars_test3()
  catEars_test4()

  alienEars_test1()
  alienEars_test2()
  alienEars_test3()
  alienEars_test4()
  alienEars_test5()

  print('[runTests] END')

def power_test1():
  printTestResult(getTestName(), power(2, 0) == 1)

def power_test2():
  printTestResult(getTestName(), power(2, 1) == 2)

def power_test3():
  printTestResult(getTestName(), power(2, 2) == 4)

def power_test4():
  printTestResult(getTestName(), power(2, 3) == 8)

def catEars_test1():
  printTestResult(getTestName(), cat_ears(0) == 0)

def catEars_test2():
  printTestResult(getTestName(), cat_ears(1) == 2)

def catEars_test3():
  printTestResult(getTestName(), cat_ears(2) == 4)

def catEars_test4():
  printTestResult(getTestName(), cat_ears(3) == 6)

def alienEars_test1():
  printTestResult(getTestName(), alien_ears(0) == None)

def alienEars_test2():
  printTestResult(getTestName(), alien_ears(1) == 3)

def alienEars_test3():
  printTestResult(getTestName(), alien_ears(2) == 5)

def alienEars_test4():
  printTestResult(getTestName(), alien_ears(3) == 8)

def alienEars_test5():
  printTestResult(getTestName(), alien_ears(4) == 10)

def printTestResult(label, testAssertion):
  if (testAssertion):
    print(f'{label} - Passed')
  else:
    print(f'{label} - Failed')

def getTestName():
  return inspect.stack()[1][3]

def power(x, y):
  if y == 0:
    return 1
  else:
    return x * power(x, y - 1)

def cat_ears(n):
  if n == 0:
    return 0
  else:
    return 2 + cat_ears(n - 1)

def alien_ears(n):
  if n <= 0:
    print('Enter a number greater than 0.')
    return

  if n == 1:
    return 3
  elif n % 2 == 0:
    return 2 + alien_ears(n - 1)
  else:
    return 3 + alien_ears(n - 1)

if __name__ == '__main__':
  main()
