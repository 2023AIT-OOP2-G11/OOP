import csv

class Character:
    def __init__(self, name, hp, mp, attack, defense, age):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.attack = attack
        self.defense = defense
        self.age = age

    def display_status(self):
        print(f"{self.name}のステータスは" +
              f"HP:{self.hp}," +
              f"MP:{self.mp}," +
              f"Atk:{self.attack}," +
              f"Def:{self.defense}," +
              f"Age:{self.age}")

class Wizard(Character):
    def __init__(self, name, hp, mp, attack, defense, age, magic_power, mp_recovery):
        super().__init__(name, hp, mp, attack, defense, age)
        self.magic_power = magic_power
        self.mp_recovery = mp_recovery

    def display_status(self):
        super().display_status()
        print(f"Magic Power:{self.magic_power}," +
              f"MP Recovery:{self.mp_recovery}")

    def recover_mp_per_turn(self):
        self.mp = min(self.mp + self.mp_recovery, self.max_mp)

def printHeroStatusWithWeapon() -> None:

    # インスタンスを作成してステータス情報を出力する
    wizard = Wizard(self, name, hp, mp, attack, defense, age, magic_power, mp_recovery)
    wizard.display_status()

if __name__ == '__main__':
    printHeroStatusWithWeapon()