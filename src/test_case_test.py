from test_case import TestCase
from was_run import WasRun

class TestCaseTest(TestCase):
  def setUp(self):
    self.sut = WasRun("testMethod")

  def testRunning(self):
    self.sut.run()
    assert(self.sut.wasRun)

  def testSetUp(self):
    self.sut.run()
    assert(self.sut.wasSetup)

TestCaseTest("testRunning").run()
TestCaseTest("testSetUp").run()
