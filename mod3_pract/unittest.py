import unittest

# def numb(n):
#     res: list[str]
#     if n <= 0:
#         raise Exception
#     res = []
#     for i in range(n, 0, -1):
#         res.append('*'* i)
#     return '\n'.join(res)

# class TestPrint(unittest.TestCase):
#     def test_test(self):
#         self.assertEqual(
#             numb(1),'''*''')
#     def test_negative(self):
#         with self.assertRaises(Exception):
#             numb(-1)
#     def test_null(self):
#         with self.assertRaises(Exception):
#             numb(0)



# def len_number(n: int) -> int:
#     if n < 0:
#         raise ValueError("Negative numbers are not allowed")
#     return len(str(n))

# class TestLenNumber(unittest.TestCase):
#     def test_positive_number(self):
#         self.assertEqual(len_number(12345), 5)

#     def test_zero(self):
#         self.assertEqual(len_number(0), 1)

#     def test_negative_number(self):
#         with self.assertRaises(ValueError):
#             len_number(-10)
#     def test_str(self):
#         with self.assertRaises(TypeError):
#             len_number("123")



# if __name__ == '__main__':
#     unittest.main()


