from modules.Character import Character
import random

class Swordsman(Character):
    def __init__(self, name, hp, attack, mp):
        super().__init__(name, hp, attack, mp)

    def special_attack(self, other):
        special_damage = self.attack * 2
        message = f"\n{self.name} の強力な突進! {other.name} に {special_damage} のダメージ!"
        print(f"\n{self.name} の強力な突進! {other.name} に {special_damage} のダメージ!")
        message += other.get_hit(special_damage)
        return message

    def block(self):
        block_value = random.randint(5, 10)
        message = f"\n{self.name} が防御態勢をとった! 次の攻撃のダメージを軽減! (軽減量: {block_value})"
        print(f"\n{self.name} が防御態勢をとった! 次の攻撃のダメージを軽減! (軽減量: {block_value})")

        return message
