from character import Character

class Enemy(Character):
  def __init__(self, name, hp, strength, defense):
    super().__init__(name, hp, strength, defense)

  def setName(self, name):
    raise Exception('Enemies cannot change their name')

  def calculateDmg(self):
    return (super().getStrength() * 0.5)
