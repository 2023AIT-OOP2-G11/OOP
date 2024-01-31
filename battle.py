# battle.py
import random
import json
from modules.Character import Character
from modules.Hero import Hero
from modules.Wizard import Wizard
from modules.Priest import Priest
from modules.Swordman import Swordsman
from modules.Monster import Monster

class Battle():
    def __init__(self):
        self.set_status()

    # キャラクターの初期状態を読み込む関数
    def __load_initial_status__(self):  
        with open('modules/status.json', 'r') as file:
            data = json.load(file)
            # debug
            print(data)
        return data
    def set_status(self):
        # ステータスファイルを読み込む
        data = self.__load_initial_status__()
        self.heros = []
        hero = Hero(data['hero'][0]['name'], data['hero'][0]['hp'], data['hero'][0]['attack'], data['hero'][0]['mp'])
        self.heros.append(hero)
        swordsman = Swordsman(data['swordsman'][0]['name'], data['swordsman'][0]['hp'], data['swordsman'][0]['attack'], data['swordsman'][0]['mp'])
        self.heros.append(swordsman)
        wizard = Wizard(data['wizard'][0]['name'], data['wizard'][0]['hp'], data['wizard'][0]['attack'], data['wizard'][0]['mp'])
        self.heros.append(wizard)
        priest = Priest(data['priest'][0]['name'], data['priest'][0]['hp'], data['priest'][0]['attack'], data['priest'][0]['mp'])
        self.heros.append(priest)
        self.monster = Monster(data['monster'][0]['name'], data['monster'][0]['hp'], data['monster'][0]['attack'], data['monster'][0]['mp'])
        # キャラクター行動ターンを指定する変数
        self.character_turn = 0

    # キャラクターのステータスを
    def get_data(self):
        return self.heros,self.monster

    def battle(self,choice):
        # 行動ターンのキャラクターのデータを取得
        hero = self.heros[self.character_turn]

        message = ""
        if choice == "1":
            # 通常攻撃
            message += hero.attack_other(self.monster)
            print(message)
        elif choice == "2":
                # 特殊攻撃またはスキルの使用
            if isinstance(hero, Hero):
                message += hero.special_attack(self.monster)
            elif isinstance(hero, Swordsman):
                message += hero.special_attack(self.monster)
            elif isinstance(hero, Wizard):
                message += hero.cast_spell(self.monster)
            elif isinstance(hero, Priest):
                message += hero.heal(random.choice(self.heros)) # 仲間をランダムに選択して回復
        elif choice == "3":
            # 防御または回避のアクション
            if isinstance(hero, Swordsman):
                message += hero.block()
            elif isinstance(hero, Wizard):
                message += hero.teleport()
            elif isinstance(hero, Priest):
                message += hero.purify()
            else:
                message += hero.heal()

        # モンスターの攻撃
        if self.monster.is_alive():
            target_hero = random.choice([hero for hero in self.heros if hero.is_alive()])
            message += self.monster.attack_other(target_hero)
        else:
            return False,"モンスターは倒されました！ヒーロたちの勝利です！",self.heros,self.monster

        cnt = 0
        for hero in self.heros:
            if hero.is_alive():
                cnt += 1
        print(cnt)
        if cnt == 0:
            return False,"ヒーロたちは倒されました！ヒーロたちの敗北です！",self.heros,self.monster
        
        if self.character_turn < 3:
            self.character_turn += 1
        else:
            self.character_turn = 0

        for hero in self.heros:
            if hero.mp + 5 <= hero.max_mp:
                hero.mp += 5
        return True,message,self.heros,self.monster    

