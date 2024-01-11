import json
import random

def decrease_stat(initial_stat):
    # 1から10のランダムな値を生成して、初期ステータスから減算
    decrease_value = random.randint(1, 10)
    result_stat = max(0, initial_stat - decrease_value)  # ステータスが負の値にならないように調整

    return result_stat

def main():
    # JSONファイルからキャラクターのステータスを読み込む
    with open('character_stats.json', 'r') as file:
        character_stats = json.load(file)

    # 各ステータスを100からランダムに減少させる
    for stat_name, stat_value in character_stats.items():
        character_stats[stat_name] = decrease_stat(stat_value)

    # 変更されたステータスを表示
    print("変更後のステータス:")
    print(json.dumps(character_stats, indent=2))

    # JSONファイルに変更を保存
    with open('character_stats_updated.json', 'w') as file:
        json.dump(character_stats, file, indent=2)

if __name__ == "__main__":
    main()