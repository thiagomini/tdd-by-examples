from test_result import TestResult


class TestCase:
    def __init__(self, name: str) -> None:
        self.name = name

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def run(self, testResult: TestResult) -> TestResult:
        testResult.testStarted()
        try:
            self.setUp()
            method = getattr(self, self.name)
            method()
        except AssertionError as exception:
            raise exception
        except Exception as unknownException:
            testResult.testFailed()

        self.tearDown()

        return testResult
