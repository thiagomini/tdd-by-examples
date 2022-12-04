from test_case import TestCase
class WasRun(TestCase):
  def __init__(self, name: str):
    self.wasRun = None
    super().__init__(name)

  def testMethod(self) -> None:
    self.wasRun = 1