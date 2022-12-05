from test_case import TestCase
from test_result import TestResult
from test_suite import TestSuite
from was_run import WasRun


class TestCaseTest(TestCase):
    def testSetUp(self):
        sut = WasRun("testMethod")
        testResult = TestResult()
        sut.run(testResult)
        assert (sut.methodCalls == ['setUp', 'testMethod', 'tearDown'])

    def testResult(self):
        sut = WasRun("testMethod")
        testResult = TestResult()
        sut.run(testResult)
        assert (testResult.summary() == '1 run, 0 failed')

    def testFailedResult(self):
        sut = WasRun("testBrokenMethod")
        testResult = TestResult()

        sut.run(testResult)
        assert (testResult.summary() == '1 run, 1 failed')

    def testFailedSetup(self):
        class TestWithBrokenSetup(TestCase):
            def __init__(self, name: str):
                super().__init__(name)

            def setUp(self):
                raise Exception

            def testMethod(self):
                pass

        sut = TestWithBrokenSetup('testMethod')
        testResult = TestResult()

        try:
            sut.run(testResult)
        except Exception:
            raise AssertionError('Should not have raised exception')

        assert (testResult.summary() == '1 run, 1 failed')

    def testSuite(self):
        suite = TestSuite()
        suite.add(WasRun('testMethod'))
        suite.add(WasRun('testBrokenMethod'))

        testResult = TestResult()
        suite.run(testResult)
        assert (testResult.summary() == "2 run, 1 failed")


suite = TestSuite()
suite.add(TestCaseTest("testSetUp"))
suite.add(TestCaseTest("testResult"))
suite.add(TestCaseTest("testFailedResult"))
suite.add(TestCaseTest("testFailedSetup"))
suite.add(TestCaseTest("testSuite"))

result = TestResult()

suite.run(result)

assert (result.summary() == '5 run, 0 failed')
