from modules.Character import Character
import random

class Priest(Character):
    def __init__(self, name, hp, attack, mp):
        super().__init__(name, hp, attack, mp)
        self.mp = mp

    def heal(self, target):
        if self.mp >= 12:
            heal_amount = random.randint(15, 25)
            self.mp -= 12
            target.hp += heal_amount
            message = f"\n{self.name} の癒しの魔法! {target.name} のHPが {heal_amount} 回復! (残りMP: {self.mp})"
            # print(f"{self.name} の癒しの魔法! {target.name} のHPが {heal_amount} 回復! (残りMP: {self.mp})")
        else:
            message = f"\n{self.name} のMPが足りず、癒しの魔法が失敗"
            # print(f"{self.name} のMPが足りず、癒しの魔法が失敗")
        return message

    def purify(self):
        message = f"\n{self.name} が味方を浄化した! 状態異常が解除された。"
        # print(f"{self.name} が味方を浄化した! 状態異常が解除された。")
        return message