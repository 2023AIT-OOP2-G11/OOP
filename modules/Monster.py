from Character import Character

class Monster(Character):
    def __init__(self, name, hp, attack, mp):
        super().__init__(name, hp, attack, mp)
        self.mp = mp