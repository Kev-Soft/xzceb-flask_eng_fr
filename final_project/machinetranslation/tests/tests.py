import unittest
from translator import frenchtoenglish, englishtofrench

class TestMethods(unittest.TestCase):

    def test_f2e1(self):
        self.assertNotEqual(frenchtoenglish(0), 0)
    
    def test_f2e2(self):
        self.assertEqual(frenchtoenglish('Bonjour'), 'Hello')

    def test_e2f1(self):
        self.assertNotEqual(englishtofrench(0), 0)

    def test_e2f2(self):
        self.assertEqual(englishtofrench('Hello'), 'Bonjour')

if __name__ == '__main__':
    unittest.main()