class WasRun:
  def __init__(self, name: str):
    self.wasRun = None
    self.name = name

  def testMethod(self) -> None:
    self.wasRun = 1

  def run(self) -> None:
    method = getattr(self, self.name)
    method()