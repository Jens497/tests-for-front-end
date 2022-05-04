import unittest
from TestBank import TestBank

if __name__ == '__main__':

    tst = TestBank()
    suite = tst.suites()
    #suite.addTest(TestBank('check_sign_up'))
    runner = unittest.TextTestRunner()
    runner.run(suite)
