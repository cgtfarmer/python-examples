import unittest

class Test1(unittest.TestCase):
  def runTest(self):
    with self.assertRaises(Exception):
      createGreeting()

class Test2(unittest.TestCase):
  def runTest(self):
    with self.assertRaises(Exception):
      createGreeting(None)

class Test3(unittest.TestCase):
  def runTest(self):
    with self.assertRaises(Exception):
      createGreeting(None, None)

class Test4(unittest.TestCase):
  def runTest(self):
    with self.assertRaises(Exception):
      createGreeting(None, "Doe")

class Test5(unittest.TestCase):
  def runTest(self):
    with self.assertRaises(Exception):
      createGreeting("John", None)

class Test6(unittest.TestCase):
  def runTest(self):
    with self.assertRaises(Exception):
      createGreeting("", "")

class Test7(unittest.TestCase):
  def runTest(self):
    with self.assertRaises(Exception):
      createGreeting("", "Doe")

class Test8(unittest.TestCase):
  def runTest(self):
    with self.assertRaises(Exception):
      createGreeting("John", "")

class Test9(unittest.TestCase):
  def runTest(self):
    expected = f'Hello John Doe, welcome home!'
    actual = createGreeting("John", "Doe")

    self.assertEqual(expected, actual)

def createGreeting(firstName, lastName):
  if (firstName == None) or (lastName == None):
    raise Exception("Params must be present")

  if (type(firstName) != str) or (type(lastName) != str):
    raise Exception("Params must be strings")

  if (firstName.strip() == "") or (lastName.strip() == ""):
    raise Exception("Params must not be empty strings")

  return f'Hello {firstName} {lastName}, welcome home!'

if __name__ == '__main__':
  unittest.main()
