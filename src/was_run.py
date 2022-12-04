from test_case import TestCase
class WasRun(TestCase):
  def __init__(self, name: str):
    self.wasRun = None
    self.wasSetup = None
    super().__init__(name)

  def testMethod(self) -> None:
    self.wasRun = 1

  def setUp(self):
    self.wasSetup = 1
