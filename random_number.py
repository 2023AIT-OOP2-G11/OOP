import random

def Random_Number(num):
    # 1からnumまでの範囲で乱数を生成
    random_number = random.randint(1, num)

    # 生成された乱数がnumの10分の1の場合、"クリティカル"と出力
    if random_number == num // 10:
        print("クリティカル")

    # 生成された乱数を出力（デバッグ用）
    print(f"{random_number}")

    return random_number

# 関数を呼び出して結果を表示
result = Random_Number(10)
print(f"{result}")
