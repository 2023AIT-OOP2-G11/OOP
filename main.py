from flask import Flask, request, render_template
import random # ランダムデータ作成のためのライブラリ
from datetime import datetime
import numpy

app = Flask(__name__)

# 1. プロジェクトのトップ
@app.route('/')
def top():
    return render_template('top.html')

@app.route('/top',methods=["POST"])
def returnTotop():
    return render_template('top.html')

# 2. ゲーム進行フォーム
@app.route('/start',methods=["POST"])
def play():
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
    # モンスタステータスの確認

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
        return render_template('end.html',message="ヒーロたちの勝ち!")

                            
# 3. ゲームエンド画面
@app.route('/start/end')
def end():
    # ゲームのエンドを呼び出し
    return render_template('end.html')

if __name__ == "__main__":

    # ゲーム進行を管理するインスタンス
    self.play = Battle()
    app.run()