import json

def read_json(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"ファイル '{file_path}' が見つかりません。")
        return None

def write_json(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

def change_hp(file_path, amount):
    # JSONファイルからデータを読み込む
    character_data = read_json(file_path)

    if character_data:
        # HPを変更する
        character_data['HP'] += amount

        # 変更を保存する
        write_json(file_path, character_data)

if __name__ == "__main__":
    file_path = "character damage result/status.json"

    # HPを5増やす例
    change_hp(file_path, 5)

    # HPを3減らす例
    change_hp(file_path, -3)