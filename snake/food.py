import settings


class Food:
    def __init__(self):
        self.energy = 0
        self.name = ''

    def promote_to_food(self, name_and_energy):
        self.energy = name_and_energy[1]
        self.name = name_and_energy[0]
        self.content = settings.FRUITS[self.name]
        self.isfood = 1
