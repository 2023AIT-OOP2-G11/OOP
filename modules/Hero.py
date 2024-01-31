from modules.Character import Character
import random

class Hero(Character):
    def __init__(self, name, hp, attack, mp):
        super().__init__(name, hp, attack, mp)
        self.mp = mp

    def special_attack(self, other):
        if self.mp >= 5:
            special_damage = self.attack * 3
            self.mp -= 5
            message = f"{self.name} の特殊攻撃 {special_damage} のダメージ! (残りMP: {self.mp})"
            message += other.get_hit(special_damage)
        else:
            message = f"{self.name} のMPが足りず、特殊攻撃が失敗"
        return message

    def heal(self):
        if self.mp >= 10:
            heal_amount = random.randint(2, 5)
            self.mp -= 10
            self.hp += heal_amount
            message = f"{self.name} の回復魔法! HPが {heal_amount} 回復! (残りMP: {self.mp})"
            #m print(f"{self.name} の回復魔法! HPが {heal_amount} 回復! (残りMP: {self.mp})")
        else:
            message = f"{self.name} のMPが足りず、回復魔法が失敗"
            # print(f"{self.name} のMPが足りず、回復魔法が失敗")
        return message