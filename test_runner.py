import os
import unittest

import time

from tests.simple_test import SimpleTest

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RESULTS_DIR = os.path.join(BASE_DIR, 'test_results')


def _generate_log_file_name() -> str:
    timestr = time.strftime("%Y%m%d-%H%M%S")
    filename = '{0}/TEST-{1}.txt'.format(RESULTS_DIR, timestr)
    return filename


def suite_simple():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(SimpleTest))
    return test_suite


# def suite_main_page():
#     test_suite = unittest.TestSuite()
#     test_suite.addTest(unittest.makeSuite(SimpleTest))
#     return test_suite


if __name__ == "__main__":
    # TODO: Add parameters for running different suits
    filename = _generate_log_file_name()
    runner = unittest.TextTestRunner()
    results = runner.run(suite_simple())

