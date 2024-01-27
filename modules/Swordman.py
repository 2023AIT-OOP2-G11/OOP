from Character import Character
import random

class Swordsman(Character):
    def __init__(self, name, hp, attack, mp):
        super().__init__(name, hp, attack, mp)

    def special_attack(self, other):
        special_damage = self.attack * 2
        print(f"\n{self.name} の強力な突進! {other.name} に {special_damage} のダメージ!")
        other.get_hit(special_damage)


    def block(self):
        block_value = random.randint(5, 10)
        print(f"\n{self.name} が防御態勢をとった! 次の攻撃からのダメージを軽減! (軽減量: {block_value})")
