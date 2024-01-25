from Character import Character
import random

class Priest(Character):
    def __init__(self, name, hp, attack, mp):
        super().__init__(name, hp, attack)
        self.mp = mp

    def heal(self, target):
        if self.mp >= 12:
            heal_amount = random.randint(15, 25)
            self.mp -= 12
            target.hp += heal_amount
            print(f"{self.name} の癒しの魔法! {target.name} のHPが {heal_amount} 回復! (残りMP: {self.mp})")
        else:
            print(f"{self.name} のMPが足りず、癒しの魔法が失敗!")

    def purify(self):
        print(f"{self.name} が味方を浄化した! 状態異常が解除された。")