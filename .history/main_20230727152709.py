from random import randint


class Character:
    def __init__(self, name):
        self.name = name

    RANGE_VALUE_ATTACK = (1, 3)

    def attack(self):
        value_attack = (5 + randint(*self.RANGE_VALUE_ATTACK))
        return (f'{self.name} нанёс противнику урон, равный '
                f'{value_attack}')

    def defence(self):
        pass

    def special(self):
        pass


class Warrior(Character):

    def attack(self):
        super().attack()

    def defence(self):
        super().defence()

    def special(self):
        super().special()


class Mage(Character):

    def attack(self):
        super().attack()

    def defence(self):
        super().defence()

    def special(self):
        super().special()


class Healer(Character):

    def attack(self):
        super().attack()

    def defence(self):
        super().defence()

    def special(self):
        super().special()
