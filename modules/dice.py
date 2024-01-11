import random

def roll_dice(number_of_dice, number_of_sides):
    """
    サイコロを振る関数
    :param number_of_dice: 振るサイコロの数
    :param number_of_sides: サイコロの面の数
    :return: 各サイコロの出た目のリスト
    """
    results = []
    for _ in range(number_of_dice):
        roll = random.randint(1, number_of_sides)
        results.append(roll)
    return results

# 例: 10面サイコロを2回振る
print(roll_dice(2, 10))

# 例: 100面サイコロを1回振る
print(roll_dice(1, 100))
