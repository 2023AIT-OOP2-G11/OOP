from math import ceil

class Character:
    def __init__(self, name, Hp, Atk, mp):
        self.name = name
        self.hp = Hp
        self.attack = Atk
        self.mp = mp

    def getJobName(self):
        return "タンク"

    def getAttack(self):
        return "攻撃"
    
    def getGuard(self):
        return "守る"

    def Attack(self, enemy):
        self.hp -= enemy
        if self.hp < 0:
            self.hp = 0

    def Guard(self, enemy):
        if self.mp >= 5:
            self.mp -= 5
        damage_reduction = 0.5
        damage = ceil(damage_reduction * enemy.attack)
        enemy.receiveDamage(damage)

if __name__ == "__main__":
        Character()