import random

class Character:
    def __init__(self, name, Hp, Atk):
        self.name = name
        self.hp = Hp
        self.attack = Atk

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

class Tank(Character):
    def attack(self, other):
        damage = self.attack * 2
        print(f"{self.name} は {damage} のダメージ!!")
        other.get_hit(damage)

    def guard(self):
        Nodamage = random.randint(5, 10)
        self.guard = Nodamage*0
        print(f"ダメージは{self.guard}。{self.name}は守りを固めている")

    def substitute(self, other):
        damage = random.randint(0, other.attack)
        print(f"{self.name}は身代わりになった。代わりにダメージを受けた。{damage}のダメージ")
        self.get_hit(damage)

def battle(tank, monster):
    while tank.is_alive() and monster.is_alive():
        print(f"\n{tank.name} のターン:")
        print("1: 攻撃")
        print("2: 守る")
        print("3: 身代わり")
    
        choice = input("どうする？ (1 or 2 or 3): ")
        if choice == '1':
            tank.attack_other(monster)
        elif choice == '2':
            tank.guard()
        elif choice == '3':
            tank.substitute(monster)
        else:
            print("1,2,3の中から行動を選んでください.")

        if monster.is_alive():
            monster.attack_other(tank)

    if tank.is_alive():
        print(f"{tank.name} 勝利!")
    else:
        print(f"{monster.name} 勝利!")

# キャラクターの作成
tank = Tank("Tank", 40, 5)
monster = Character("Goblin", 30, 3)

# バトルの開始
battle(tank, monster)
