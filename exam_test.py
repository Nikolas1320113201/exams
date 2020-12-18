import unittest
from Maxvalue import exam

class TestProgression(unittest.TestCase):
  test= [2,3,6,4,3]
    
  def max_in_list_test(lst):
    self.assertEqual(lst.max_in_list(test), 6)

if __name__ == "__main__":
  unittest.main()
