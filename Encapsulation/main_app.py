'''
Encapsulasi :
1. Membuat semua variable private
2. Akses variable menggunakan getter
3. Setting variable menggunakan setter

Sehingga encapsulation berfungsi untuk menjaga nilai variable tetap menjadi konsisten saat program berjalan
'''

class Hero:

    def __init__(self, name, health, attPower) -> None:
        self.__name = name
        self.__health = health
        self.__attPower = attPower

    # Getter
    def getName(self):
        return self.__name
    
    def getHealth(self):
        return self.__health

    # Setter
    def diserang(self, powerSerangan):
        self.__health -= powerSerangan
    

zilong = Hero("Zilong", 90, 100)

print(zilong.__dict__)

# Start Game
print(zilong.getName())
print(zilong.getHealth())
zilong.diserang(10)
print(zilong.getHealth())