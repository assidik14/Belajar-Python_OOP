class Hero():

    def __init__(self, name, health, attack, armor) -> None:
        self.name = name
        self.health = health
        self.attack = attack
        self.armor = armor
    
    def serang(self, lawan):
        print(f"{self.name} menyerang {lawan.name}")
        print(20*"=")
        lawan.diserang(self)
    
    def diserang(self, musuh):
        print(f"{self.name} diserang {musuh.name}")
        damage = musuh.attack / self.armor
        self.health -= damage
        print(f"Serangan diterima = {damage}")
        print(f"Darah {self.name} sekarang = {self.health}")


layla = Hero("Layla", 80, 100, 10)
balmond = Hero("Balmond", 100, 80, 40)

layla.serang(balmond)
print("\n")
balmond.serang(layla)
print("\n")
balmond.serang(layla)
