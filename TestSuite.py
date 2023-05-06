import requests
import HtmlTestRunner

import unittest
import HtmlTestRunner

import API_tests
from API_tests import ApiTests


class TestSuite(unittest.TestCase):

    def test_suite(self):
        tests_to_run = unittest.TestSuite()
        tests_to_run.addTests([unittest.defaultTestLoader.loadTestsFromTestCase(ApiTests)])
        #Expected type 'Type[TestCase]', got'API_tests.py' instead


        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True, # vrem sa ne genereze un singur raport pentru toate clasele
            report_title="Test Execution Report",
            report_name="Test Results"
        )

        runner.run(tests_to_run)