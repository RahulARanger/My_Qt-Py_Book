import RashSetup.__RashModules__.Rash.ApplicationManager
from .MemeGen import *


class UTIL(TabWindow):
    def __init__(self, shared: dict):
        Rash: RashSetup.__RashModules__.Rash.ApplicationManager.RashMain = shared["RASH"]
        super().__init__(Rash)

        self.Generator = MemeGenerator(self)
        self.easeAdd(self.Generator, "SpongeBob")
