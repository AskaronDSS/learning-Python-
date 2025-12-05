import unittest

def numb(n):
    res: list[str]
    if n <= 0:
        raise Exception
    res = []
    for i in range(n, 0, -1):
        res.append('*'* i)
    return '\n'.join(res)

class TestPrint(unittest.TestCase):
    def test_test(self):
        self.assertEqual(
            numb(1),'''*''')
    def test_negative(self):
        with self.assertRaises(Exception):
            numb(-1)
    def test_null(self):
        with self.assertRaises(Exception):
            numb(0)



if __name__ == '__main__':
    unittest.main()