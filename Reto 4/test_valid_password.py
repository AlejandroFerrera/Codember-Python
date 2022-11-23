from valid_password import is_valid_password
import unittest

class TestEncrypt(unittest.TestCase):
    def test_1(self):
        self.assertEqual(is_valid_password(55678), True)
    
    def test_2(self):
        self.assertEqual(is_valid_password(12555), True)
    
    def test_3(self):
        self.assertEqual(is_valid_password(55555), True)
    
    def test_4(self):
        self.assertEqual(is_valid_password(12345), False)
    
    def test_5(self):
        self.assertEqual(is_valid_password(57775), False)
    
if __name__ == '__main__':
    unittest.main()


