import unittest
from zebra import zebra

class TestEncrypt(unittest.TestCase):
    def test_1(self):
        self.assertEqual(zebra(['red', 'blue', 'red', 'blue', 'green']), [4, 'blue'])
    
    def test_2(self):
        self.assertEqual(zebra(['green', 'red', 'blue', 'gray']), [2, 'gray'])
    
    def test_3(self):
        self.assertEqual(zebra(['blue', 'blue', 'blue', 'blue']), [1, 'blue'])
    
    def test_4(self):
        self.assertEqual(zebra(['red', 'green', 'red', 'green', 'red', 'green']), [6, 'green'])
    
    def test_5(self):
        self.assertEqual(zebra(['blue', 'red', 'blue', 'red', 'gray']), [4, 'red'])
    
    def test_6(self):
        self.assertEqual(zebra(['red', 'red', 'blue', 'red', 'red', 'red', 'green']), [3, 'red'])
    
    def test_7(self):
        self.assertEqual(zebra(['red', 'blue', 'red', 'green', 'red', 'green', 'red', 'green']), [6, 'green'])
    
if __name__ == '__main__':
    unittest.main()
