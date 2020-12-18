import unittest
from Calculator import exam

class TestCalculator(unittest.TestCase):
  def __init__(self):
    self.calculator = Calculator()
    
  def n_chlen(self):
    self.assertEqual(self.calculator.add(3), 9)
    self.assertEqual(self.calculator.add(4), 11)

if __name__ == "__main__":
  unittest.main()
