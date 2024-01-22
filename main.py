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

# 2. startフォーム
@app.route('/start',methods=["POST"])
def start():
    # 入力画面のテンプレートを呼び出し
    return render_template('start.html')

# 2. ゲームスキル送信先、ゲーム進行フォーム
@app.route('/start/play',methods=["POST"])
def play():
    message:list() = []  # メッセージを格納す
    result:bool() = True  # スキルの選択チェック結果を格納する変数

    # スタート画面で選択されたデータを受け取る
    yuusya_skill:int() = request.form.get("yuusya", None)
    mahou_skill:int() = request.form.get("mahou", None)
    kennshi_skill:int() = request.form.get("kennshi", None)
    kaifuku_skill:int() = request.form.get("kaifuku", None)

    # 各職業のスキルが選択されていない場合、メッセージを追加し、resultをFalseにする
    if yuusya_skill == None:
        message.append("勇者のスキルを選択してください")
        result = False
    elif mahou_skill == None:
        message.append("魔法使いのスキルを選択してください")
        result = False
    elif kennshi_skill == None:
        message.append("剣士のスキルを選択してください")
        result = False
    elif kaifuku_skill == None:
        message.append("僧侶のスキルを選択してください")
        result = False

    # ゲーム画面を呼び出す
    return render_template('game.html', 
                            result=result,
                            message=message,
                            yuusya_skill=yuusya_skill,
                            mahou_skill=mahou_skill,
                            kennshi_skill=kennshi_skill,
                            kaifuku_skill=kaifuku_skill)
                            
# 3. ゲームエンド画面
@app.route('/start/play/end')
def end():
    # ゲームのエンドを呼び出し
    return render_template('end.html')

if __name__ == "__main__":
    app.run()