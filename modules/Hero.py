from Character import Character
import random

class Hero(Character):
    def __init__(self, name, hp, attack, mp):
        super().__init__(name, hp, attack, mp)
        self.mp = mp

    def special_attack(self, other):
        if self.mp >= 5:
            special_damage = self.attack * 2
            self.mp -= 5
            print(f"{self.name} の特殊攻撃 {special_damage} のダメージ! (残りMP: {self.mp})")
            other.get_hit(special_damage)
        else:
            print(f"{self.name} のMPが足りず、特殊攻撃が失敗")

    def heal(self):
        if self.mp >= 10:
            heal_amount = random.randint(5, 10)
            self.mp -= 10
            self.hp += heal_amount
            print(f"{self.name} の回復魔法! HPが {heal_amount} 回復! (残りMP: {self.mp})")
        else:
            print(f"{self.name} のMPが足りず、回復魔法が失敗")