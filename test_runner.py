import unittest

from tests.simple_test import SimpleTest


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(SimpleTest))
    return suite


def suite_main():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(SimpleTest))
    return suite


if __name__ == "__main__":
    # TODO: Add parameters for running different suits
    runner = unittest.TextTestRunner().run(suite())
