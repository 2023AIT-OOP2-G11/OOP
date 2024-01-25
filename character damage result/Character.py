import random
#これはゲーム内のすべてのキャラクターの基本クラス
#名前、ヒットポイント（hp）、攻撃力などの属性を持っている

class Character:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack

    def is_alive(self):
        return self.hp > 0

    def get_hit(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        print(f"{self.name} の残りHP: {self.hp}")

    def attack_other(self, other):
        damage = random.randint(0, self.attack)
        print(f"{self.name} の通常攻撃 {other.name} に {damage} のダメージ!")
        other.get_hit(damage)