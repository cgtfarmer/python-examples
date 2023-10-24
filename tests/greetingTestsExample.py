import inspect

def main():
  runTests()
  print(createGreeting("Jane", "Doe"))

def runTests():
  test1()
  test2()
  test3()
  test4()
  test5()
  test6()
  test7()
  test8()

def test1():
  # printTestResult(getTestName(), createGreeting()) # Throws exception
  return

def test2():
  # printTestResult(getTestName(), createGreeting(None)) # Throws exception
  return

def test3():
  # printTestResult(getTestName(), createGreeting(None, None)) # Throws exception
  return

def test4():
  # printTestResult(getTestName(), createGreeting(None, "Doe")) # Throws exception
  return

def test5():
  # printTestResult(getTestName(), createGreeting("John", None) # Throws exception
  return

def test6():
  # printTestResult(getTestName(), createGreeting("", "Doe")) # Throws exception
  return

def test7():
  # printTestResult(getTestName(), createGreeting("John", "") # Throws exception
  return

def test8():
  expected = f'Hello John Doe, welcome home!'
  actual = createGreeting("John", "Doe")

  testAssertion = (expected == actual)
  printTestResult(getTestName(), testAssertion)

def printTestResult(label, testAssertion):
  if (testAssertion):
    print(f'{label} - Passed')
  else:
    print(f'{label} - Failed')

def getTestName():
  return inspect.stack()[1][3]

def createGreeting(firstName, lastName):
  if (firstName == None) or (lastName == None):
    raise Exception("Params must be present")

  if (type(firstName) != str) or (type(lastName) != str):
    raise Exception("Params must be strings")

  if (firstName.strip() == "") or (lastName.strip() == ""):
    raise Exception("Params must not be empty strings")

  return f'Hello {firstName} {lastName}, welcome home!'

if __name__ == '__main__':
  main()
