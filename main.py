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
    kenshi_skill:str() = request.form.get("kenshi", None)
    tannku_skill:str() = request.form.get("tannku", None)
    shienn_skill:str() = request.form.get("shienn", None)
    kaifuku_skill:str() = request.form.get("kaifuku", None)

    # 各職業のスキルが選択されていない場合、メッセージを追加し、resultをFalseにする
    if kenshi_skill == None:
        message.append("剣士のスキルを選択してください")
        result = False
    elif tannku_skill == None:
        message.append("タンク役のスキルを選択してください")
        result = False
    elif shienn_skill == None:
        message.append("支援役のスキルを選択してください")
        result = False
    elif kaifuku_skill == None:
        message.append("回復役のスキルを選択してください")
        result = False

    # ゲーム画面を呼び出す
    return render_template('game.html', 
                            result=result,
                            message=message,
                            kenshi_skill=kenshi_skill,
                            shienn_skill=shienn_skill,
                            tannku_skill=tannku_skill,
                            kaifuku_skill=kaifuku_skill)
                            
# 3. ゲームエンド画面
@app.route('/start/play/end')
def end():
    # ゲームのエンドを呼び出し
    return render_template('end.html')

if __name__ == "__main__":
    app.run()