import json

def printTankStatus() -> None:

    # ヒーローデータの読み込み
    tank_header = []
    tank_data = []
    json_file_path = 'status.json'
    with open('status.json') as f:
        reader = json.load(f)
        for row in reader:
            if len(tank_header) == 0:
                tank_header = row
            else:
                tank_data.append(row)

    # 出力処理
    for tank in tank_data:
        if tank[0] == '1': # idが1の場合
            print(f"{tank[1]}のステータスは" +
            f"HP:{tank[2]}," +
            f"MP:{tank[3]}," +
            f"Atk:{tank[4]}," +
            f"Def:{tank[5]}," +
            f"Age:{tank[6]}")

    for tank in tank_data:
        if tank[0] == '2': # idが2の場合
            print(f"{tank[1]}のステータスは" +
            f"HP:{tank[2]}," +
            f"MP:{tank[3]}," +
            f"Atk:{tank[4]}," +
            f"Def:{tank[5]}," +
            f"Age:{tank[6]}")

    for tank in tank_data:
        if tank[0] == '3': # idが3の場合
            print(f"{tank[1]}のステータスは" +
            f"HP:{tank[2]}," +
            f"MP:{tank[3]}," +
            f"Atk:{tank[4]}," +
            f"Def:{tank[5]}," +
            f"Age:{tank[6]}")    

def printTankStatusWithWeapon() -> None:

    # ヒーローデータの読み込み
    tank_header = []
    tank_data = []
    with open('status.json') as f:
        reader = json.reader(f)
        for row in reader:
            if len(hero_header) == 0:
                hero_header = row
            else:
                tank_data.append(row)
    
    # 変数に保存する
    # for文の中で代入する前に外で変数を宣言する
    tank_name = None
    tank_hp = None
    tank_mp = None
    tank_atk = None
    tank_def = None
    tank_age = None
    for hero in tank_data: # hero_dataはcsv読み取りなので何行入っているかわからない
        if hero[0] == '1': # idが1のとき代入
            hero_name = hero[1]
            hero_hp = int(hero[2])
            hero_mp = int(hero[3])
            hero_atk = int(hero[4])
            hero_def = int(hero[5])
            hero_age = int(hero[6])

    # 武器データの読み込み
    weapon_header = []
    weapon_data = []
    with open('lecture02_Weapon.csv') as f:
        reader = json.reader(f)
        for row in reader:
            if len(weapon_header) == 0:
                 weapon_header = row
            else:
                 weapon_data.append(row)

    # 変数に保存する
    w = list(filter(lambda x: x[0] == weapon_data))[0]
    # ステータスを文字から数値へ変換
    w[2:7] = list(map(int, w[2:7]))
    # listの一部を変数へ代入
    weapon_name,weapon_hp,weapon_mp,weapon_atk,weapon_def,weapon_age = w[1:7]

    # 以下のようにheroと同様の方法で変数に保存してもOK
    #for weapon in weapon_data: # weapon_dataはcsv読み取りなので何行入っているかわからない
    #    if weapon[0] == hero_weapon:
    #        weapon_name = int(weapon[1])
    #        weapon_hp = int(weapon[2])
    #        weapon_mp = int(weapon[3])
    #        weapon_atk = int(weapon[4])
    #        weapon_def = int(weapon[5])
    #        weapon_age = int(weapon[6])

    # ステータス情報を出力する
    print(f"{weapon_name}を装備した{hero_name}のステータスは" +
        f"HP:{tank_hp+weapon_hp}," +
        f"MP:{tank_mp+weapon_mp}," +
        f"Atk:{tank_atk+weapon_atk}," +
        f"Def:{tank_def+weapon_def}," +
        f"Age:{tank_age+weapon_age}")


if __name__ == '__main__':
    printTankStatus()
    printTankStatusWithWeapon()