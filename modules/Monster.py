<<<<<<< Updated upstream
from modules.Character import Character

class Monster(Character):
    def __init__(self, name, hp, attack, mp):
        super().__init__(name, hp, attack, mp)
=======
from Character import Character

class Monster(Character):
    def __init__(self, name, hp, attack, mp):
        super().__init__(name, hp, attack)
>>>>>>> Stashed changes
        self.mp = mp