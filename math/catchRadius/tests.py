import unittest

from main import isInCatchRadius

class IsInCatchRadiusTests(unittest.TestCase):
  def test_1(self):
    with self.assertRaises(Exception):
      isInCatchRadius(None, 1, 1, 1, 1)

  def test_2(self):
    with self.assertRaises(Exception):
      isInCatchRadius(1, None, 1, 1, 1)

  def test_3(self):
    with self.assertRaises(Exception):
      isInCatchRadius(1, 1, None, 1, 1)

  def test_4(self):
    with self.assertRaises(Exception):
      isInCatchRadius(1, 1, 1, None, 1)

  def test_5(self):
    with self.assertRaises(Exception):
      isInCatchRadius(1, 1, 1, 1, None)

  def test_6(self):
    with self.assertRaises(Exception):
      isInCatchRadius("1", 1, 1, 1, 1)

  def test_7(self):
    with self.assertRaises(Exception):
      isInCatchRadius(1, "1", 1, 1, 1)

  def test_8(self):
    with self.assertRaises(Exception):
      isInCatchRadius(1, 1, "1", 1, 1)

  def test_9(self):
    with self.assertRaises(Exception):
      isInCatchRadius(1, 1, 1, "1", 1)

  def test_10(self):
    with self.assertRaises(Exception):
      isInCatchRadius(1, 1, 1, 1, "1")

  def test_11(self):
    expected = True
    actual = isInCatchRadius(0, 0, 3, 0, 0)
    self.assertEqual(expected, actual)

  def test_12(self):
    expected = True
    actual = isInCatchRadius(0, 0, 3, 1, 1)
    self.assertEqual(expected, actual)

  def test_13(self):
    expected = True
    actual = isInCatchRadius(0, 0, 3, 0, 3)
    self.assertEqual(expected, actual)

  def test_14(self):
    expected = True
    actual = isInCatchRadius(0, 0, 3, 3, 0)
    self.assertEqual(expected, actual)

  def test_15(self):
    expected = True
    actual = isInCatchRadius(0, 0, 3, -3, 0)
    self.assertEqual(expected, actual)

  def test_16(self):
    expected = False
    actual = isInCatchRadius(0, 0, 3, -3, -3)
    self.assertEqual(expected, actual)

  def test_17(self):
    expected = True
    actual = isInCatchRadius(0, 0, 3, -1, -1)
    self.assertEqual(expected, actual)

  def test_18(self):
    expected = False
    actual = isInCatchRadius(0, 0, 3, -4, -1)
    self.assertEqual(expected, actual)

  def test_19(self):
    expected = False
    actual = isInCatchRadius(0, 0, 3, -1, -4)
    self.assertEqual(expected, actual)

  def test_20(self):
    expected = False
    actual = isInCatchRadius(-45, 111, 5, -50, 116)
    self.assertEqual(expected, actual)

  def test_21(self):
    expected = False
    actual = isInCatchRadius(-45, 111, 5, -50, 115)
    self.assertEqual(expected, actual)

  def test_22(self):
    expected = False
    actual = isInCatchRadius(0, 0, 3, 3, 3)
    self.assertEqual(expected, actual)

  def test_23(self):
    expected = False
    actual = isInCatchRadius(0, 0, 3, -3, 3)
    self.assertEqual(expected, actual)

  def test_24(self):
    expected = False
    actual = isInCatchRadius(0, 0, 3, 3, -3)
    self.assertEqual(expected, actual)

  def test_25(self):
    expected = False
    actual = isInCatchRadius(0, 0, 3, 3, 2)
    self.assertEqual(expected, actual)

  def test_26(self):
    expected = False
    actual = isInCatchRadius(0, 0, 5, -5, 5)
    self.assertEqual(expected, actual)

  def test_27(self):
    expected = False
    actual = isInCatchRadius(0, 0, 5, 5, 5)
    self.assertEqual(expected, actual)

  def test_28(self):
    expected = False
    actual = isInCatchRadius(0, 0, 5, -5, -5)
    self.assertEqual(expected, actual)

  def test_29(self):
    expected = False
    actual = isInCatchRadius(0, 0, 5, 5, -5)
    self.assertEqual(expected, actual)

  def test_30(self):
    expected = True
    actual = isInCatchRadius(77, 133, 17, 85, 120)
    self.assertEqual(expected, actual)

if __name__ == '__main__':
  unittest.main()
