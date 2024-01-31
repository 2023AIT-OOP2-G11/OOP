from modules.Character import Character

class Monster(Character):
    def __init__(self, name, hp, attack, mp):
        super().__init__(name, hp, attack, mp)

    def special_attack(self, other):
        if self.mp >= 5:
            special_damage = self.attack * 2
            self.mp -= 5
            message = f"{self.name} の特殊攻撃 {special_damage} のダメージ! (残りMP: {self.mp})"
            message += other.get_hit(special_damage)
        else:
            message = f"{self.name} のMPが足りず、特殊攻撃が失敗"
        return message
