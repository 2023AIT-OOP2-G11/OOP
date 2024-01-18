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
        print(f"{self.name} の攻撃 {other.name} に {damage} のダメージ!")
        other.get_hit(damage)

class Hero(Character):
    def special_attack(self, other):
        special_damage = self.attack * 2
        print(f"{self.name} の特殊攻撃の {special_damage} のダメージ!!")
        other.get_hit(special_damage)

    def heal(self):
        heal_amount = random.randint(5, 10)
        self.hp += heal_amount
        print(f"{self.name} のHPが {heal_amount} 回復!")

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
            print("Invalid choice. Please try again.")

        if monster.is_alive():
            monster.attack_other(hero)

    if hero.is_alive():
        print(f"{hero.name} 勝利!")
    else:
        print(f"{monster.name} 勝利!")

# キャラクターの作成
hero = Hero("Hero", 40, 5)
monster = Character("Goblin", 30, 3)

# バトルの開始
battle(hero, monster)
