class Hero():
    # Class Variable
    jumlah_hero = 0

    # Instance Variable
    def __init__(self, inputName, inputHealth, inputAttack, inputArmor):
      self.name = inputName
      self.health = inputHealth
      self.attack = inputAttack
      self.armor = inputArmor
      Hero.jumlah_hero += 1

    # Methode tanpa argumen, void method
    def siapa(self):
       print("Namaku adalah " + self.name)
    
    # Methode dengan argumen
    def healthUp(self, up):
       self.health += up
    
    # Methode dengan return
    def getHealth(self):
       return self.health

# Create Hero    
hero1 = Hero("Gatotkaca", 100, 80, 90)
hero2 = Hero("Leyley", 80, 100, 70)

# Akses method
hero2.siapa()
print(hero2.getHealth())
hero2.healthUp(10)
print(hero2.getHealth())