import random
#これはゲーム内のすべてのキャラクターの基本クラス
#名前、ヒットポイント（hp）、攻撃力などの属性を持っている

class Character:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack

    def is_alive(self):
        return self.hp > 0

    def get_hit(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        print(f"{self.name} の残りHP: {self.hp}")

    def attack_other(self, other):
        damage = random.randint(0, self.attack)
        print(f"\n{self.name} の通常攻撃 : {other.name} に {damage} のダメージ!")
        other.get_hit(damage)

#Character クラスを継承し、魔法ポイント（mp）という新しい属性を追加
class Hero(Character):
    def __init__(self, name, hp, attack, mp):
        super().__init__(name, hp, attack)
        self.mp = mp

    def special_attack(self, other):
        if self.mp >= 5:
            special_damage = self.attack * 2
            self.mp -= 5
            print(f"\n{self.name} の特殊攻撃 {special_damage} のダメージ! (残りMP: {self.mp})")
            other.get_hit(special_damage)
        else:
            print(f"\n{self.name} のMPが足りず、特殊攻撃が失敗!")

    def heal(self):
        if self.mp >= 10:
            heal_amount = random.randint(5, 10)
            self.mp -= 10
            self.hp += heal_amount
            print(f"\n{self.name} の回復魔法! HPが {heal_amount} 回復! (残りMP: {self.mp})")
        else:
            print(f"\n{self.name} のMPが足りず、回復魔法が失敗!")
            
#Hero と同様に、これらのクラスは Character を継承し、キャラクタータイプに固有の追加の属性やメソッドを持つ可能性があります。
#is_alive: キャラクターが生きているかどうかをヒットポイントを基に確認します。get_hit: キャラクターがダメージを受けたときにヒットポイントを更新します。
#attack_other: ランダムなダメージで他のキャラクターに通常攻撃をシミュレートします。
class Swordsman(Character):
    def __init__(self, name, hp, attack):
        super().__init__(name, hp, attack)

    def special_attack(self, other):
        special_damage = self.attack * 2
        print(f"\n{self.name} の強力な突進! {other.name} に {special_damage} のダメージ!")
        other.get_hit(special_damage)


    def block(self):
        block_value = random.randint(5, 10)
        print(f"\n{self.name} が防御態勢をとった! 次の攻撃からのダメージを軽減! (軽減量: {block_value})")

class Wizard(Character):
    def __init__(self, name, hp, attack, mp):
        super().__init__(name, hp, attack)
        self.mp = mp

    def cast_spell(self, other):
        if self.mp >= 8:
            spell_damage = random.randint(10, 20)
            self.mp -= 8
            print(f"\n{self.name} が魔法を唱えた! {other.name} に {spell_damage} のダメージ! (残りMP: {self.mp})")
            other.get_hit(spell_damage)
        else:
            print(f"\n{self.name} のMPが足りず、魔法が失敗!")

    def teleport(self):
        print(f"\n{self.name} がテレポートして攻撃を回避した!")

class Priest(Character):
    def __init__(self, name, hp, attack, mp):
        super().__init__(name, hp, attack)
        self.mp = mp

    def heal(self, target):
        if self.mp >= 12:
            heal_amount = random.randint(15, 25)
            self.mp -= 12
            target.hp += heal_amount
            print(f"\n{self.name} の癒しの魔法! {target.name} のHPが {heal_amount} 回復! (残りMP: {self.mp})")
        else:
            print(f"\n{self.name} のMPが足りず、癒しの魔法が失敗!")

    def purify(self):
        print(f"\n{self.name} が味方を浄化した! 状態異常が解除された。")

class Monster(Character):
    def special_attack(self, other):
        if random.random() < 0.4:  # 40%の確率で特殊攻撃
            special_damage = self.attack * 2
            print(f"\n{self.name} の特殊攻撃! {other.name} に {special_damage} のダメージ!")
            other.get_hit(special_damage)
        else:
            self.attack_other(other)

#一連のヒーローとモンスターとの戦闘をシミュレートするメイン関数です。
#各ヒーローをグループ内で反復処理し、アクション（通常攻撃、特殊攻撃、またはキャラクター固有のアクション）を選択できるようにします。
        
def battle(heroes, monster,):
    while all(hero.is_alive() for hero in heroes) and monster.is_alive():
        for hero in heroes:
            print(f"\n{hero.name} のターン:")
            print("1: 通常攻撃")
            print("2: 特殊攻撃")
            if isinstance(hero, Hero):  
                print("3: 回復")
            elif isinstance(hero, Swordsman):
                print("3: 防御")
            elif isinstance(hero, Wizard):
                print("3: 魔法")
            elif isinstance(hero, Priest):
                print("3: 癒し")

            choice = input("どうする？ (1, 2, or 3): ")
            if choice == '1':
                hero.attack_other(monster)
            elif choice == '2':
                if isinstance(hero, Hero):
                    hero.special_attack(monster)
                elif isinstance(hero, Swordsman):
                    hero.special_attack(monster)
                elif isinstance(hero, Wizard):
                    hero.cast_spell(monster)
                elif isinstance(hero, Priest):
                    hero.purify()
            elif choice == '3' and isinstance(hero, Hero):
                hero.heal()
            elif choice == '3' and isinstance(hero, Swordsman):
                hero.block()
            elif choice == '3' and isinstance(hero, Wizard):
                hero.teleport()
            elif choice == '3' and isinstance(hero, Priest):
                hero.heal(random.choice(heroes))
            else:
                print("そのコマンドは無効です！")

        if monster.is_alive():
            # モンスターの攻撃
            target_hero = random.choice(heroes)
            monster.attack_other(target_hero)

    if all(hero.is_alive() for hero in heroes):
        print(f"\n{', '.join(hero.name for hero in heroes)} たちの勝ち!")
    else:
        print(f"\n{', '.join(hero.name for hero in heroes)} たちは敗北した...")


#バトル関数は実行されたアクションとバトルの結果を出力します。
#このコードは基本的なオブジェクト指向プログラミングの概念を示しており、異なるキャラクタータイプを持つターン制のバトルシナリオをシミュレートしています。
        
# キャラクターの作成
hero = Hero("勇者", 50, 20, 20)
swordsman = Swordsman("剣士", 60, 15)
wizard = Wizard("魔法使い", 45, 6, 50)
priest = Priest("僧侶", 50, 4, 25)
monster = Character("モンスター", 150, 40)

# バトルの開始
battle([hero, swordsman, wizard, priest], monster)
