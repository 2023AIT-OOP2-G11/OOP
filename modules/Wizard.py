from Character import Character
import random

class Wizard(Character):
    def __init__(self, name, hp, attack, mp):
        super().__init__(name, hp, attack)
        self.mp = mp

    def cast_spell(self, other):
        if self.mp >= 8:
            spell_damage = random.randint(10, 20)
            self.mp -= 8
            print(f"\n{self.name} が魔法を唱えた! {other.name} に {spell_damage} のダメージ! (残りMP: {self.mp})")
            other.get_hit(spell_damage)
        else:
            print(f"\n{self.name} のMPが足りず、魔法が失敗")

    def teleport(self):
        print(f"\n{self.name} がテレポートして攻撃を回避した!")
