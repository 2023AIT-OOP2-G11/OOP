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

    def attack_other(self, other):
        damage = random.randint(0, self.attack)
        print(f"{self.name} の通常攻撃 {other.name} に {damage} のダメージ!")
        other.get_hit(damage)

class Wizard(Character):
    def __init__(self, name, hp, mp, magic_attack):
        super().__init__(name, hp, 0)  # 魔法使いの通常攻撃は使わないので0に設定
        self.mp = mp
        self.magic_attack = magic_attack

    def display_status(self):
        super().display_status()
        print(f"MP:{self.mp}")

    def cast_spell(self, other):
        if self.mp >= 5:
            damage = random.randint(0, self.magic_attack)
            print(f"{self.name} の魔法攻撃 {other.name} に {damage} のダメージ!")
            other.get_hit(damage)
            self.mp -= 5
        else:
            print("MPが足りません。通常攻撃します。")
            self.attack_other(other)

    def heal(self):
        heal_amount = random.randint(5, 10)
        self.hp = min(self.hp + heal_amount, self.max_hp)
        print(f"{self.name} の回復スキル！HPが {heal_amount} 回復しました。")

def battle(wizard, monster):
    while wizard.is_alive() and monster.is_alive():
        print(f"\n{wizard.name} のターン:")
        print("1: 通常攻撃")
        print("2: 魔法攻撃")
        print("3: 回復")
    
        choice = input("どうする？ (1 or 2 or 3): ")
        if choice == '1':
            wizard.attack_other(monster)
        elif choice == '2':
            wizard.cast_spell(monster)
        elif choice == '3':
            wizard.heal()
        else:
            print("1か2か3を選んでください.")

        if monster.is_alive():
            monster.attack_other(wizard)

    if wizard.is_alive():
        print(f"{wizard.name} 勝利!")
    else:
        print(f"{monster.name} 勝利!")

# キャラクターの作成
wizard = Wizard("Wizard", 40, 20, 8)
monster = Character("Goblin", 30, 3)

# バトルの開始
battle(wizard, monster)