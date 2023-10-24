import unittest

class CreateGreetingTests(unittest.TestCase):
  def setUp(self):
    # print("Common setup code goes here")
    return

  def tearDown(self):
    # print("Common teardown code goes here")
    return

  def test_1(self):
    with self.assertRaises(Exception):
      createGreeting()

  def test_2(self):
    with self.assertRaises(Exception):
      createGreeting(None)

  def test_3(self):
    with self.assertRaises(Exception):
      createGreeting(None, None)

  def test_4(self):
    with self.assertRaises(Exception):
      createGreeting(None, "Doe")

  def test_5(self):
    with self.assertRaises(Exception):
      createGreeting("John", None)

  def test_6(self):
    with self.assertRaises(Exception):
      createGreeting("", "")

  def test_7(self):
    with self.assertRaises(Exception):
      createGreeting("", "Doe")

  def test_8(self):
    with self.assertRaises(Exception):
      createGreeting("John", "")

  def test_9(self):
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
