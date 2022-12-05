from typing import List
from test_case import TestCase
from test_result import TestResult

class TestSuite():
  def __init__(self) -> None:
    self.tests: List[TestCase] = []

  def add(self, testCase: TestCase):
    self.tests.append(testCase)

  def run(self, testResult: TestResult):
    for test in self.tests:
      test.run(testResult)
