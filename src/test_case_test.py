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

TestCaseTest("testSetUp").run()
TestCaseTest("testResult").run()
