import random

class Character:
    def __init__(self, name, hp, mp, attack):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.max_mp = mp
        self.attack = attack

    def is_alive(self):
        return self.hp > 0

    def get_hit(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def use_mp(self, cost):
        if self.mp >= cost:
            self.mp -= cost
            return True
        else:
            print(f"{self.name} のMPが不足しています!")
            return False

    def attack_other(self, other):
        damage = random.randint(0, self.attack)
        print(f"{self.name} の通常攻撃 {other.name} に {damage} のダメージ!")
        other.get_hit(damage)

    def magic_attack(self, other):
        if self.use_mp(8):  # 魔法攻撃のMPコストを8と仮定
            magic_damage = random.randint(8, 12)
            print(f"{self.name} の魔法攻撃 {other.name} に {magic_damage} のダメージ!")
            other.get_hit(magic_damage)

    def heal(self):
        heal_amount = random.randint(5, 10)
        self.hp += heal_amount
        print(f"{self.name} のHPが {heal_amount} 回復!")

class Wizard(Character):
    def __init__(self, name):
        super().__init__(name, hp=40, mp=20, attack=5)

    def special_attack(self, other):
        print("魔法使いの特殊攻撃！")
        self.magic_attack(other)

class Monster(Character):
    def __init__(self, name, hp, mp, attack):
        super().__init__(name, hp, mp, attack)

    def roar(self):
        print(f"{self.name} は怖い声を上げて攻撃力が上昇した!")

    def attack_other(self, other):
        super().attack_other(other)
        if random.random() < 0.3:  # 30%の確率で怒りモード
            self.roar()
            self.attack *= 1.5  # 攻撃力が1.5倍に上昇

def battle(wizard, monsters):
    print("戦闘開始!")
    while wizard.is_alive() and any(monster.is_alive() for monster in monsters):
        print(f"\n{wizard.name} のターン:")
        print("1: 通常攻撃")
        print("2: 魔法攻撃")
        print("3: 回復")

        choice = input("どうする？ (1, 2, or 3): ")
        if choice == '1':
            wizard.attack_other(random.choice(monsters))
        elif choice == '2':
            wizard.magic_attack(random.choice(monsters))
        elif choice == '3':
            wizard.heal()
        else:
            print("Invalid choice. Please try again.")

        for monster in monsters:
            if monster.is_alive():
                monster.attack_other(wizard)

    if wizard.is_alive():
        print(f"{wizard.name} 勝利!")
    else:
        print("モンスターたちの勝利!")

# 複数のモンスターを作成
monster1 = Monster("Goblin1", 30, 10, 3)
monster2 = Monster("Goblin2", 30, 10, 3)
monster3 = Monster("Big Goblin", 40, 15, 5)

# バトルの開始
wizard = Wizard("魔法使い")
battle(wizard, [monster1, monster2, monster3])