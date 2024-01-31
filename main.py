from flask import Flask, request, render_template
import random # ランダムデータ作成のためのライブラリ
from datetime import datetime
import numpy

app = Flask(__name__)

# 1. プロジェクトのトップ
@app.route('/')
def top():
    return render_template('top.html')

# エンド画面からトップ画面に戻った場合
@app.route('/top',methods=["POST"])
def returnTotop():
    return render_template('top.html')

# 2. ゲームフォーム初期読み込み
@app.route('/start',methods=["POST"])
def start():
    # バトルインスタンスから各キャラクターのステータスを取得する
    # ゲーム画面を呼び出す
    # debug
    return render_template('game.html', 
                            message='test',
                            monster_hp=100,
                            hero_hp=100,
                            swordsman_hp=100,
                            wizard_hp=100,
                            priest_hp=100,
                            hero_mp=100,
                            swordsman_mp=100,
                            wizard_mp=100,
                            priest_mp=100
                            )

# 3. ゲーム進行フォーム
@app.route('/game/play',methods=["POST"])
def game():
    choice = request.form.get('skill')
    # ゲーム画面を呼び出す
    return render_template('game.html', 
                            message=choice,
                            monster_hp=100,
                                        hero_hp=100,
                                        swordsman_hp=100,
                                        wizard_hp=100,
                                        priest_hp=100,
                                        hero_mp=100,
                                        swordsman_mp=100,
                                        wizard_mp=100,
                                        priest_mp=100
                                        )
    # バトルメソッドを呼び出し、選択した数値を渡す                              
    self.play.battle(choice)

    """ # ゲーム画面を呼び出す
    if play.monster.is_alive():
        # キャラクタステータスを確認
        if all(hero.is_alive() for hero in heroes):
            # game画面が選択したボタンを取得する
            choice = request.form.get('skill')
            if choice==-1:
                # ゲーム画面を呼び出す
                return render_template('game.html', 
                                        message='test',
                                        monster_hp=100,
                                        hero_hp=100,
                                        swordsman_hp=100,
                                        wizard_hp=100,
                                        priest_hp=100,
                                        hero_mp=100,
                                        swordsman_mp=100,
                                        wizard_mp=100,
                                        priest_mp=100
                                        )
            else:
                self.play(choice)
            # ゲーム画面を呼び出す
            return render_template('game.html', 
                                    message=message,
                                    monster_hp=monster_hp,
                                    hero_hp=hero_hp,
                                    swordsman_hp=swordsman_hp,
                                    wizard_hp=wizard_hp,
                                    priest_hp=priest_hp,
                                    hero_mp=hero_mp,
                                    swordsman_mp=swordsman_mp,
                                    wizard_mp=wizard_mp,
                                    priest_mp=priest_mp
                                    )
        # キャラクターが倒された
        else:
            # エンド画面を呼び出す
            return render_template('end.html',message="ヒーロたちは敗北した...")
    # モンスタが倒された場合
    else:
        # エンド画面を呼び出す
        return render_template('end.html',message="ヒーロたちの勝ち!") """
            
# 4. ゲームエンド画面
@app.route('/start/end')
def end():
    # ゲームのエンドを呼び出し
    return render_template('end.html')

if __name__ == "__main__":
    # ゲーム進行を管理するインスタンス
    # self.play = Battle()
    app.run()