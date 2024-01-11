from flask import Flask, request, render_template
import random # ランダムデータ作成のためのライブラリ
from datetime import datetime
import numpy

app = Flask(__name__)

# 1. プロジェクトのトップ
@app.route('/')
def top():
    return render_template('top.html')


# 2. startフォーム
@app.route('/start')
def start():
    # 入力画面のテンプレートを呼び出し
    return render_template('start.html')



#仮
# 2. ゲーム進行フォーム
@app.route('/start/play')
def game():
    # ゲーム画面を呼び出し
    return render_template('play.html')


# 3. ゲームエンド画面
@app.route('/start/play/end')
def end():
    # ゲームのエンドを呼び出し
    return render_template('end.html')


if __name__ == "__main__":
    app.run()