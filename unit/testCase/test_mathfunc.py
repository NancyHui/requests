import unittest
from unit.mathfunc import *


class TestMathFunc(unittest.TestCase):
    """Test mathfunc.py"""
    # # ************************ every case ****************************
    # # 覆写unittest.TestCase中的setUp()和tearDown()方法，每个case执行前后都执行一次
    # def setUp(self):
    #     print("do something before test.Prepare enviroment")
    #
    # def tearDown(self):
    #     print("do something after test.Clean up")
    # # **************************************************************

    # ****************************************************************************
    # 在所有case执行之前准备一次环境，在所有case执行完毕之后再清理环境
    @classmethod
    def setUpClass(cls):
        print("This setUpClass() method only called once.")

    @classmethod
    def tearDownClass(cls):
        print("This tearDownClass() method only called once either.")

    # *****************************************************************************

    def test_add(self):
        """Test method add(a, b)"""
        print("add")
        self.assertEqual(3, add(1, 2))
        self.assertNotEqual(3, add(2, 2))

    def test_minus(self):
        """Test method minus(a, b)"""
        print("minus")
        self.assertEqual(1, minus(3, 2))

    def test_multi(self):
        """Test method multi(a, b)"""
        print("multi")
        self.assertEqual(6, multi(2, 3))

    def test_divide(self):
        """Test method divide(a, b)"""
        print("divide")
        self.assertEqual(2, divide(6, 3))
        self.assertEqual(2.5, divide(5, 2))


# if __name__ == '__main__':
#     unittest.main(verbosity=2)