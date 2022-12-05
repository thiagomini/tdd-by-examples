from test_case import TestCase
from was_run import WasRun

class TestCaseTest(TestCase):
  def testSetUp(self):
    sut = WasRun("testMethod")
    sut.run()
    assert(sut.methodCalls == ['setUp', 'testMethod', 'tearDown'])

  def testResult(self):
    sut = WasRun("testMethod")
    result = sut.run()
    assert(result.summary() == '1 run, 0 failed')

  def testFailedResult(self):
    sut = WasRun("testBrokenMethod")
    result = sut.run()
    assert(result.summary() == '1 run, 1 failed')

TestCaseTest("testSetUp").run()
TestCaseTest("testResult").run()
TestCaseTest("testFailedResult").run()
