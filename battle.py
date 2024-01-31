# battle.py
import random
import json
from modules.Character import Character
from modules.Hero import Hero
from modules.Wizard import Wizard
from modules.Priest import Priest
from modules.Swordman import Swordsman
from modules.Monster import Monster

# バトルのシミュレーションを行う関数
def battle(heroes, monster, choice):
    for hero in heroes:
        if hero.is_alive():
            if choice == '1':
                # 通常攻撃
                hero.attack_other(monster)
            elif choice == '2':
                # 特殊攻撃またはスキルの使用
                if isinstance(hero, Hero):
                    hero.special_attack(monster)
                elif isinstance(hero, Swordsman):
                    hero.special_attack(monster)
                elif isinstance(hero, Wizard):
                    hero.cast_spell(monster)
                elif isinstance(hero, Priest):
                    hero.heal(random.choice(heroes)) # 仲間をランダムに選択して回復
            elif choice == '3':
                # 防御または回避のアクション
                if isinstance(hero, Swordsman):
                    hero.block()
                elif isinstance(hero, Wizard):
                    hero.teleport()
                elif isinstance(hero, Priest):
                    hero.purify()

    # モンスターの攻撃
    if monster.is_alive():
        target_hero = random.choice([hero for hero in heroes if hero.is_alive()])
        monster.attack_other(target_hero)

# JSONファイルからデータを読み込む
with open('status.json', 'r') as file:
    data = json.load(file)

# キャラクターのインスタンスを作成
hero_data = data["hero"][0]
swordsman_data = data["swordsman"][0]
wizard_data = data["wizard"][0]
priest_data = data["priest"][0]
monster_data = data["monster"][0]

hero = Hero(hero_data["name"], hero_data["hp"], hero_data["attack"], hero_data["mp"])
swordsman = Swordsman(swordsman_data["name"], swordsman_data["hp"], swordsman_data["attack"], swordsman_data["mp"])
wizard = Wizard(wizard_data["name"], wizard_data["hp"], wizard_data["attack"], wizard_data["mp"])
priest = Priest(priest_data["name"], priest_data["hp"], priest_data["attack"], priest_data["mp"])
monster = Monster(monster_data["name"], monster_data["hp"], monster_data["attack"], monster_data["mp"])

# バトルの開始
battle([hero, swordsman, wizard, priest], monster)


# import random
# import json
# from modules.Character import Character
# from modules.Hero import Hero
# from modules.Wizard import Wizard
# from modules.Priest import Priest
# from modules.Swordman import Swordsman
# from modules.Monster import Monster

# # class Character:
# #     def __init__(self, name, hp, attack, mp):
# #         self.name = name
# #         self.hp = hp
# #         self.attack = attack
# #         self.mp = mp

# #     def is_alive(self):
# #         return self.hp > 0

# #     def get_hit(self, damage):
# #         self.hp -= damage
# #         if self.hp < 0:
# #             self.hp = 0
# #         print(f"{self.name} の残りHP: {self.hp}")

# #     def attack_other(self, other):
# #         damage = random.randint(0, self.attack)
# #         print(f"\n{self.name} の通常攻撃 : {other.name} に {damage} のダメージ!")
# #         other.get_hit(damage)
# #     #プレイヤー
# #     def getHP(self):
# #         return self.hp
# #     def getMP(self):
# #         return self.mp
   
# # class Hero(Character):
# #     def __init__(self, name, hp, attack, mp):
# #         super().__init__(name, hp, attack)
# #         self.mp = mp

# #     def special_attack(self, other):
# #         if self.mp >= 5:
# #             special_damage = self.attack * 2
# #             self.mp -= 5
# #             print(f"\n{self.name} の特殊攻撃 {special_damage} のダメージ! (残りMP: {self.mp})")
# #             other.get_hit(special_damage)
# #         else:
# #             print(f"\n{self.name} のMPが足りず、特殊攻撃が失敗!")

# #     def heal(self):
# #         if self.mp >= 10:
# #             heal_amount = random.randint(5, 10)
# #             self.mp -= 10
# #             self.hp += heal_amount
# #             print(f"\n{self.name} の回復魔法! HPが {heal_amount} 回復! (残りMP: {self.mp})")
# #         else:
# #             print(f"\n{self.name} のMPが足りず、回復魔法が失敗!")
            
# # #Hero と同様に、これらのクラスは Character を継承し、キャラクタータイプに固有の追加の属性やメソッドを持つ可能性があります。
# # #is_alive: キャラクターが生きているかどうかをヒットポイントを基に確認します。get_hit: キャラクターがダメージを受けたときにヒットポイントを更新します。
# # #attack_other: ランダムなダメージで他のキャラクターに通常攻撃をシミュレートします。
# # class Swordsman(Character):
# #     def __init__(self, name, hp, attack, mp):
# #         super().__init__(name, hp, attack, mp)

# #     def special_attack(self, other):
# #         special_damage = self.attack * 2
# #         print(f"\n{self.name} の強力な突進! {other.name} に {special_damage} のダメージ!")
# #         other.get_hit(special_damage)


# #     def block(self):
# #         block_value = random.randint(5, 10)
# #         print(f"\n{self.name} が防御態勢をとった! 次の攻撃からのダメージを軽減! (軽減量: {block_value})")

# # class Wizard(Character):
# #     def __init__(self, name, hp, attack, mp):
# #         super().__init__(name, hp, attack)
# #         self.mp = mp

# #     def cast_spell(self, other):
# #         if self.mp >= 8:
# #             spell_damage = random.randint(10, 20)
# #             self.mp -= 8
# #             print(f"\n{self.name} が魔法を唱えた! {other.name} に {spell_damage} のダメージ! (残りMP: {self.mp})")
# #             other.get_hit(spell_damage)
# #         else:
# #             print(f"\n{self.name} のMPが足りず、魔法が失敗!")

# #     def teleport(self):
# #         print(f"\n{self.name} がテレポートして攻撃を回避した!")

# # class Priest(Character):
# #     def __init__(self, name, hp, attack, mp):
# #         super().__init__(name, hp, attack)
# #         self.mp = mp

# #     def heal(self, target):
# #         if self.mp >= 12:
# #             heal_amount = random.randint(15, 25)
# #             self.mp -= 12
# #             target.hp += heal_amount
# #             print(f"\n{self.name} の癒しの魔法! {target.name} のHPが {heal_amount} 回復! (残りMP: {self.mp})")
# #         else:
# #             print(f"\n{self.name} のMPが足りず、癒しの魔法が失敗!")

# #     def purify(self):
# #         print(f"\n{self.name} が味方を浄化した! 状態異常が解除された。")

# # class Monster(Character):
# #     def special_attack(self, other):
# #         if random.random() < 0.4:  # 40%の確率で特殊攻撃
# #             special_damage = self.attack * 2
# #             print(f"\n{self.name} の特殊攻撃! {other.name} に {special_damage} のダメージ!")
# #             other.get_hit(special_damage)
# #         else:
# #             self.attack_other(other)

# # class Monster(Character):
# #     def __init__(self, name, hp, attack, mp):
# #         super().__init__(name, hp, attack)
# #         self.mp = mp

# #一連のヒーローとモンスターとの戦闘をシミュレートするメイン関数です。
# #各ヒーローをグループ内で反復処理し、アクション（通常攻撃、特殊攻撃、またはキャラクター固有のアクション）を選択できるようにします。
        
# def battle(heroes, monster, choice):
#     if choice == '1':
#         hero.attack_other(monster)
#     elif choice == '2':
#         if isinstance(hero, Hero):
#             hero.special_attack(monster)
#         elif isinstance(hero, Swordsman):
#             hero.special_attack(monster)
#         elif isinstance(hero, Wizard):
#             hero.cast_spell(monster)
#         elif isinstance(hero, Priest):
#             hero.purify()
#     elif choice == '3' and isinstance(hero, Hero):
#         hero.heal()
#     elif choice == '3' and isinstance(hero, Swordsman):
#         hero.block()
#     elif choice == '3' and isinstance(hero, Wizard):
#         hero.teleport()
#     elif choice == '3' and isinstance(hero, Priest):
#         hero.heal(random.choice(heroes))

#     if monster.is_alive():
#             # モンスターの攻撃
#             target_hero = random.choice(heroes)
#             monster.attack_other(target_hero)

# # JSONファイルからデータを読み込む
# with open('status.json', 'r') as file:
#     data = json.load(file)

# # 各キャラクターのデータを取得し、対応するクラスのインスタンスを作成
# hero_data = data["hero"][0]
# swordsman_data = data["swordsman"][0]
# wizard_data = data["wizard"][0]
# priest_data = data["priest"][0]
# monster_data = data["monster"][0]

# # キャラクターのクラスごとに適切なインスタンスを作成
# hero = Hero(hero_data["name"], hero_data["hp"], hero_data["attack"], hero_data["mp"])
# swordsman = Swordsman(swordsman_data["name"], swordsman_data["hp"], swordsman_data["attack"], swordsman_data["mp"])
# wizard = Wizard(wizard_data["name"], wizard_data["hp"], wizard_data["attack"], wizard_data["mp"])
# priest = Priest(priest_data["name"], priest_data["hp"], priest_data["attack"], priest_data["mp"])
# monster = Monster(monster_data["name"], monster_data["hp"], monster_data["attack"], monster_data["mp"])
# # # キャラクターの作成
# # hero = Hero("勇者", 40, 5, 20)
# # swordsman = Swordsman("剣士", 35, 8, 0)
# # wizard = Wizard("魔法使い", 30, 6, 15)
# # priest = Priest("僧侶", 30, 4, 25)
# # monster = Character("モンスター", 30, 3, 0)

# # バトルの開始
# battle([hero, swordsman, wizard, priest], monster)
    
# #モンスターの特殊行動
# #class Monster(Character):
#  #   def special_attack(self, other):
#   #      if random.random() < 0.3:  # 30%の確率で特殊攻撃
#    #         special_damage = self.attack * 2
#     #        print(f"{self.name} に {special_damage} の痛恨のダメージ!")
#      #       other.get_hit(special_damage)
#       #  else:
#        #     self.attack_other(other)

