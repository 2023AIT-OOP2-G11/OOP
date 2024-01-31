from modules.Character import Character
import random

class Wizard(Character):
    def __init__(self, name, hp, attack, mp):
        super().__init__(name, hp, attack, mp)
        self.mp = mp

    def cast_spell(self, other):
        if self.mp >= 8:
            spell_damage = random.randint(10, 20)
            self.mp -= 8
            message = f"\n{self.name} が魔法を唱えた! {other.name} に {spell_damage} のダメージ! (残りMP: {self.mp})"
            print(f"\n{self.name} が魔法を唱えた! {other.name} に {spell_damage} のダメージ! (残りMP: {self.mp})")
            message += other.get_hit(spell_damage)
        else:
            message = f"\n{self.name} のMPが足りず、魔法が失敗"
            print(f"\n{self.name} のMPが足りず、魔法が失敗")

        return message

    def teleport(self):
        message = f"\n{self.name} がテレポートして攻撃を回避した!"
        print(f"\n{self.name} がテレポートして攻撃を回避した!")
        return message
