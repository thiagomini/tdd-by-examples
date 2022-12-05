from test_case import TestCase
class WasRun(TestCase):
  def __init__(self, name: str):
    self.wasRun: bool = None
    self.methodCalls = []
    super().__init__(name)

  def testMethod(self) -> None:
    self.methodCalls.append('testMethod')
    self.wasRun = 1

  def setUp(self):
    self.wasRun = False
    self.methodCalls.append('setUp')

  def tearDown(self):
    self.methodCalls.append('tearDown')
