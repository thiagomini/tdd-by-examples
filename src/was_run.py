from test_case import TestCase
class WasRun(TestCase):
  def __init__(self, name: str):
    self.wasRun: bool = None
    self.wasSetup: bool = None
    super().__init__(name)

  def testMethod(self) -> None:
    self.wasRun = 1

  def setUp(self):
    self.wasRun = False
    self.wasSetup = 1
