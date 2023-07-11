import unittest


def sum(a, b):
    return a + b


class SumTest(unittest.TestCase):
    def setUp(self):
        print("SETUP CALL")
        self.a = 10
        self.b = 20

    def tearDown(self):
        self.a = 0
        self.b = 0
        print("teardown called")

    def test_sumfunc_1(self):
        print("TEST1  CALL")

        result = sum(self.a, self.b)
        self.assertEqual(result, self.a + self.b)

    def test_sumfunc_2(self):
        print("TEST2  CALL")
        result = sum(self.b, self.a)
        self.assertEqual(result, self.b + self.a)


if __name__ == "__main__":
    unittest.main()
