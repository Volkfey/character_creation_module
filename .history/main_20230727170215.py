from random import randint

DEFAULT_ATTACK = 5
DEFAULT_DEFENCE = 10
SPECIAL_SKILL = 'Удача'
SPECIAL_BUFF = 15
BRIEF_DESC_CHAR_CLASS = 'отважный любитель приключений'


class Character:

    RANGE_VALUE_ATTACK = (1, 3)
    RANGE_VALUE_DEFENCE = (1, 5)

    def __init__(self, name):
        self.name = name

    def attack(self):
        value_attack = (DEFAULT_ATTACK + randint(*self.RANGE_VALUE_ATTACK))
        return (f'{self.name} нанёс противнику урон, равный {value_attack}')

    def defence(self):
        value_defence = (DEFAULT_DEFENCE + randint(*self.RANGE_VALUE_DEFENCE))
        return (f'{self.name} блокировал {value_defence} ед. урона.')

    def special(self):
        return (f'{self.name} применил специальное умение '
                f'"{SPECIAL_BUFF} {SPECIAL_SKILL}".')

    def __str__(self):
        if __class__.__name__ == 'warrior':
            return ('Воитель — дерзкий воин ближнего боя. '
                    'Сильный, выносливый и отважный.')
        elif __class__.__name__ == 'mage':
            return ('Маг — находчивый воин дальнего боя. '
                    'Обладает высоким интеллектом.')
        elif __class__.__name__ == 'healer':
            return ('Лекарь — могущественный заклинатель. '
                    'Черпает силы из природы, веры и духов.')
        return BRIEF_DESC_CHAR_CLASS


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
