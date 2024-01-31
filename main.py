from flask import Flask, request, render_template
import json
from battle import Battle

app = Flask(__name__)

@app.route('/')
def top():
    return render_template('top.html')

@app.route('/top', methods=["POST"])
def returntop():
    return render_template('top.html')

# ルートの外で Battle インスタンスを作成
battle = Battle()

@app.route('/start', methods=["POST"])
def start():
    heros,monster = battle.get_data()
    return render_template('game.html', heros=heros, monster=monster)

@app.route('/game/play', methods=["POST"])
def game():
    choice = request.form.get('skill')
    print('選択したボタン：' + str(choice))

    # 選択したボタンの値をbattleインスタンスに渡す
    result,message,heros,monster = battle.battle(choice)

    # モンスターが倒された場合の処理
    if result == False:
        return render_template('end.html', message=message)

    # 戦闘を続行
    return render_template('game.html', heros=heros, monster=monster,message=message)

@app.route('/start/end')
def end():
    return render_template('end.html')

if __name__ == "__main__":
    # バトルを実際に行うインスタンス
    app.run()