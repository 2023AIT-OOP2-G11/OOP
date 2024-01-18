import random

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
        print(f"{self.name} の攻撃 {other.name} に {damage} のダメージ!")
        other.get_hit(damage)

class Hero(Character):
    def __init__(self, name, hp, attack, mp):
        super().__init__(name, hp, attack)
        self.mp = mp

    def special_attack(self, other):
        if self.mp >= 5:
            special_damage = self.attack * 2
            self.mp -= 5
            print(f"{self.name} の特殊攻撃 {special_damage} のダメージ! (残りMP: {self.mp})")
            other.get_hit(special_damage)
        else:
            print(f"{self.name} のMPが足りず、失敗!")

    def heal(self):
        if self.mp >= 3:
            heal_amount = random.randint(20, 50)
            self.mp -= 3
            self.hp += heal_amount
            print(f"{self.name} のHPが {heal_amount} 回復! (残りMP: {self.mp})")
            print(f"{self.name} の残りHP: {self.hp}")
        else:
            print(f"{self.name} のMPが足りず、失敗!")

class Monster(Character):
    def special_attack(self, other):
        if random.random() < 0.3:  # 30%の確率で特殊攻撃
            special_damage = self.attack * 2
            print(f"{self.name} に {special_damage} の痛恨のダメージ!")
            other.get_hit(special_damage)
        else:
            self.attack_other(other)

def battle(hero, monster):
    while hero.is_alive() and monster.is_alive():
        print(f"\n{hero.name} のターン:")
        print("1: 攻撃")
        print("2: 特殊攻撃")
        print("3: 回復")

        choice = input("どうする？ (1, 2, or 3): ")
        if choice == '1':
            hero.attack_other(monster)
        elif choice == '2':
            hero.special_attack(monster)
        elif choice == '3':
            hero.heal()
        else:
            print("それは使えないよ!")

        if monster.is_alive():
            monster.special_attack(hero)  # モンスターの攻撃（通常または特殊）

    if hero.is_alive():
        print(f"{hero.name} たちの勝利!")
    else:
        print(f"{hero.name} たちは敗北した...")

# キャラクターの作成
hero = Hero("Hero", 100, 15, 20) #左からHP, ATK, MP
monster = Monster("Goblin", 80, 20)

# バトルの開始
battle(hero, monster)
