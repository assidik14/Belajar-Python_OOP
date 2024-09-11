class Hero:
    # Public class variable
    jumlah = 0

    # Private class variable
    __jumlah_private = 0


    def __init__(self, nama, health) -> None:
        # Public variable instance
        self.name = nama
        self.health = health

        # Private variable instance
        self.__private = "Private"

        # Protected variable instance
        self._protect = "Protected"


balmond = Hero("Balmond", 100)

print(Hero.__dict__)
print(balmond.__dict__)