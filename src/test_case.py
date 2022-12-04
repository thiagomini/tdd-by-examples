class TestCase:
  def __init__(self, name: str) -> None:
    self.name = name

  def setUp(self):
    pass

  def run(self) -> None:
    self.setUp()
    method = getattr(self, self.name)
    method()
