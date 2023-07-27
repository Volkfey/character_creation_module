class Character:
    def __init__(self, name):
        self.name = name

    def attack(self):
        pass

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
