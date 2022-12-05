from test_case import TestCase
from was_run import WasRun

class TestCaseTest(TestCase):
  def testSetUp(self):
    sut = WasRun("testMethod")
    sut.run()
    assert(sut.methodCalls == ['setUp', 'testMethod', 'tearDown'])

TestCaseTest("testSetUp").run()
