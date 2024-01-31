from flask import Flask, request, render_template
import json
from battle import battle
import battle

app = Flask(__name__)

# キャラクターの初期状態を読み込む関数
def load_initial_status():
    with open('modules/status.json', 'r') as file:
        data = json.load(file)

        # debug
        print(data)
        print(data['hero'][0]['name'])
        print(data['hero'][0]['hp'])
        print(data['hero'][0]['mp'])
    return data

@app.route('/')
def top():
    return render_template('top.html')

@app.route('/start', methods=["POST"])
def start():
    data = load_initial_status()
    print(data)
    print(data['hero'][0]['name'])
    print(data['hero'][0]['hp'])
    print(data['hero'][0]['mp'])
    return render_template('game.html', data=data)

@app.route('/game/play', methods=["POST"])
def game():
    choice = request.form.get('skill')
    print('選択したスキル：' + str(choice))
    data = load_initial_status()

    # 勇者のデータを取得（例として）
    hero = data['characters'][0]

    if choice == 'attack':
        # 通常攻撃の場合、モンスターのHPからヒーローの攻撃力を引く
        data['monster']['hp'] -= hero['attack']
    else:
        # スキルを使用する場合
        skill_index = int(choice) - 1
        skill = hero['skills'][skill_index]

        if hero['mp'] >= skill['mp_cost']:
            # MPが足りる場合、スキルを使用
            hero['mp'] -= skill['mp_cost']

            if 'damage' in skill:
                # スキルによるダメージ
                data['monster']['hp'] -= skill['damage']
            elif 'defense_boost' in skill:
                # 防御ブースト
                hero['hp'] += skill['defense_boost']
            elif 'healing' in skill:
                # 回復
                hero['hp'] += skill['healing']
        else:
            # MPが足りない場合、スキルの使用に失敗
            pass

    # モンスターが倒された場合の処理
    if data['monster']['hp'] <= 0:
        return render_template('end.html', message="ヒーロたちの勝ち！")

    # キャラクターが倒された場合の処理（すべてのキャラクターのHPをチェック）
    if all(hero['hp'] <= 0 for hero in data['characters']):
        return render_template('end.html', message="ヒーロたちは敗北した...")

    # 戦闘を続行
    return render_template('game.html', data=data)

@app.route('/start/end')
def end():
    return render_template('end.html')

if __name__ == "__main__":
    app.run()

# from flask import Flask, request, render_template
# import random # ランダムデータ作成のためのライブラリ
# from datetime import datetime
# import numpy
# from battle import battle


# app = Flask(__name__)

# # 1. プロジェクトのトップ
# @app.route('/')
# def top():
#     return render_template('top.html')

# # エンド画面からトップ画面に戻った場合
# @app.route('/top',methods=["POST"])
# def returnTotop():
#     return render_template('top.html')

# # 2. ゲーム進行フォーム
# @app.route('/start',methods=["POST"])
# def start():
#      # ゲーム画面を呼び出す
#     return render_template('game.html', 
#                             message='test',
#                             monster_hp=100,
#                             hero_hp=100,
#                             swordsman_hp=100,
#                             wizard_hp=100,
#                             priest_hp=100,
#                             hero_mp=100,
#                             swordsman_mp=100,
#                             wizard_mp=100,
#                             priest_mp=100
#                             )
# # # ゲームの初期化
# # def initialize_game():
# #     # JSONファイルからデータを読み込む
# #     with open('status.json', 'r') as file:
# #         data = json.load(file)

# #     # 各キャラクターのデータを取得し、対応するクラスのインスタンスを作成
# #     hero_data = data["hero"][0]
# #     swordsman_data = data["swordsman"][0]
# #     wizard_data = data["wizard"][0]
# #     priest_data = data["priest"][0]
# #     monster_data = data["monster"][0]

# #     # キャラクターのクラスごとに適切なインスタンスを作成
# #     hero = Hero(hero_data["name"], hero_data["hp"], hero_data["attack"], hero_data["mp"])
# #     swordsman = Swordsman(swordsman_data["name"], swordsman_data["hp"], swordsman_data["attack"], swordsman_data["mp"])
# #     wizard = Wizard(wizard_data["name"], wizard_data["hp"], wizard_data["attack"], wizard_data["mp"])
# #     priest = Priest(priest_data["name"], priest_data["hp"], priest_data["attack"], priest_data["mp"])
# #     monster = Monster(monster_data["name"], monster_data["hp"], monster_data["attack"], monster_data["mp"])
    
# #     return [hero, swordsman, wizard, priest], monster

# # # ゲームの初期化
# # heroes, monster = initialize_game()

# # 1. プロジェクトのトップ
# # @app.route('/')
# # def top():
# #     return render_template('top.html')

# # # エンド画面からトップ画面に戻った場合
# # @app.route('/top', methods=["POST"])
# # def return_to_top():
# #     return render_template('top.html')

# # # 2. ゲーム進行フォーム
# # @app.route('/start', methods=["POST"])
# # def start():
# #     # ゲーム画面を呼び出す
# #     return render_template('game.html', 
# #                             message='Choose your action',
# #                             monster_hp=monster.hp,
# #                             hero_hp=heroes[0].hp,
# #                             swordsman_hp=heroes[1].hp,
# #                             wizard_hp=heroes[2].hp,
# #                             priest_hp=heroes[3].hp,
# #                             hero_mp=heroes[0].mp,
# #                             swordsman_mp=heroes[1].mp,
# #                             wizard_mp=heroes[2].mp,
# #                             priest_mp=heroes[3].mp
# #                             )

# # # 2. ゲーム進行フォーム
# # @app.route('/game/play', methods=["POST"])
# # def game():
# #     if monster.is_alive():
# #         # キャラクタステータスを確認
# #         if all(hero.is_alive() for hero in heroes):
# #             # game画面が選択したボタンを取得する
# #             choice = request.form.get('skill')
# #             if choice == '-1':
# #                 # ゲーム画面を呼び出す
# #                 return render_template('game.html', 
# #                                         message='Choose your action',
# #                                         monster_hp=monster.hp,
# #                                         hero_hp=heroes[0].hp,
# #                                         swordsman_hp=heroes[1].hp,
# #                                         wizard_hp=heroes[2].hp,
# #                                         priest_hp=heroes[3].hp,
# #                                         hero_mp=heroes[0].mp,
# #                                         swordsman_mp=heroes[1].mp,
# #                                         wizard_mp=heroes[2].mp,
# #                                         priest_mp=heroes[3].mp
# #                                         )
# #             else:
# #                 battle(heroes, monster, choice)
# #             # ゲーム画面を呼び出す
# #             return render_template('game.html', 
# #                                     message='Choose your action',
# #                                     monster_hp=monster.hp,
# #                                     hero_hp=heroes[0].hp,
# #                                     swordsman_hp=heroes[1].hp,
# #                                     wizard_hp=heroes[2].hp,
# #                                     priest_hp=heroes[3].hp,
# #                                     hero_mp=heroes[0].mp,
# #                                     swordsman_mp=heroes[1].mp,
# #                                     wizard_mp=heroes[2].mp,
# #                                     priest_mp=heroes[3].mp
# #                                     )
# #         # キャラクターが倒された
# #         else:
# #             # エンド画面を呼び出す
# #             return render_template('end.html', message="ヒーロたちは敗北した...")
# #     # モンスタが倒された場合
# #     else:
# #         # エンド画面を呼び出す
# #         return render_template('end.html', message="ヒーロたちの勝ち!")
            
# # # 3. ゲームエンド画面
# # @app.route('/start/end')
# # def end():
# #     # ゲームのエンドを呼び出し
# #     return render_template('end.html')

# # if __name__ == "__main__":
# #     app.run()



# # 2. ゲーム進行フォーム
# @app.route('/game/play',methods=["POST"])
# def game():
#     if play.monster.is_alive():
#         # キャラクタステータスを確認
#         if all(hero.is_alive() for hero in heroes):
#             # game画面が選択したボタンを取得する
#             choice = request.form.get('skill')
#             if choice==-1:
#                 # ゲーム画面を呼び出す
#                 return render_template('game.html', 
#                                         message='test',
#                                         monster_hp=100,
#                                         hero_hp=100,
#                                         swordsman_hp=100,
#                                         wizard_hp=100,
#                                         priest_hp=100,
#                                         hero_mp=100,
#                                         swordsman_mp=100,
#                                         wizard_mp=100,
#                                         priest_mp=100
#                                         )
#             else:
#                 self.play(choice)
#             # ゲーム画面を呼び出す
#             return render_template('game.html', 
#                                     message=message,
#                                     monster_hp=monster_hp,
#                                     hero_hp=hero_hp,
#                                     swordsman_hp=swordsman_hp,
#                                     wizard_hp=wizard_hp,
#                                     priest_hp=priest_hp,
#                                     hero_mp=hero_mp,
#                                     swordsman_mp=swordsman_mp,
#                                     wizard_mp=wizard_mp,
#                                     priest_mp=priest_mp
#                                     )
#         # キャラクターが倒された
#         else:
#             # エンド画面を呼び出す
#             return render_template('end.html',message="ヒーロたちは敗北した...")
#     # モンスタが倒された場合
#     else:
#         # エンド画面を呼び出す
#         return render_template('end.html',message="ヒーロたちの勝ち!")
            
# # 3. ゲームエンド画面
# @app.route('/start/end')
# def end():
#     # ゲームのエンドを呼び出し
#     return render_template('end.html')

# if __name__ == "__main__":
#     # ゲーム進行を管理するインスタンス
#     # self.play = Battle()
#     app.run()