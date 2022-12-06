from test_case import TestCase
from test_result import TestResult
from test_suite import TestSuite
from was_run import WasRun


class TestCaseTest(TestCase):

    def setUp(self):
        self.result = TestResult()

    def testSetUp(self):
        sut = WasRun("testMethod")
        sut.run(self.result)
        assert (sut.methodCalls == ['setUp', 'testMethod', 'tearDown'])

    def testResult(self):
        sut = WasRun("testMethod")
        sut.run(self.result)
        assert (self.result.summary() == '1 run, 0 failed')

    def testFailedResult(self):
        sut = WasRun("testBrokenMethod")
        sut.run(self.result)
        assert (self.result.summary() == '1 run, 1 failed')

    def testFailedSetup(self):
        class TestWithBrokenSetup(TestCase):
            def __init__(self, name: str):
                super().__init__(name)

            def setUp(self):
                raise Exception

            def testMethod(self):
                pass

        sut = TestWithBrokenSetup('testMethod')

        try:
            sut.run(self.result)
        except Exception:
            raise AssertionError('Should not have raised exception')

        assert (self.result.summary() == '1 run, 1 failed')

    def testSuite(self):
        suite = TestSuite()
        suite.add(WasRun('testMethod'))
        suite.add(WasRun('testBrokenMethod'))

        suite.run(self.result)
        assert (self.result.summary() == "2 run, 1 failed")


suite = TestSuite()
suite.add(TestCaseTest("testSetUp"))
suite.add(TestCaseTest("testResult"))
suite.add(TestCaseTest("testFailedResult"))
suite.add(TestCaseTest("testFailedSetup"))
suite.add(TestCaseTest("testSuite"))

result = TestResult()

suite.run(result)

testSummary = result.summary()

print(testSummary)
assert (testSummary == '5 run, 0 failed')
