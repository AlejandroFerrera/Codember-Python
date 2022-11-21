from encrypt import decrypt
import unittest

class TestEncrypt(unittest.TestCase):
    def test_1(self):
        self.assertEqual(decrypt("109105100117"), 'midu')
    
    def test_2(self):
        self.assertEqual(decrypt("9911110010110998101114"), 'codember')
    
    def test_3(self):
        self.assertEqual(decrypt("9911110010110998101114 109105100117"), 'codember midu')
    
    def test_4(self):
        self.assertEqual(decrypt("11210897121 116101116114105115"), 'play tetris')
    
if __name__ == '__main__':
    unittest.main()