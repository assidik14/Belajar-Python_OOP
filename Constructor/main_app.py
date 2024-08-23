class Friends():
    
    def __init__(self, InputNama, InputKota, InpitKelamin) -> None:
        self.nama = InputNama       # Ini sama saja dengan 'object'.nama
        self.kota = InputKota       # Ini sama saja dengan 'object'.kota
        self.kelamin = InpitKelamin # Ini sama saja dengan 'object'.kelamin

# Jadi kita bisa buat gini :
object1 = Friends("Samsul","Jakarta","Laki-laki")
object2 = Friends("Odah","Bandung","Perempuan")

# Print semua atribut masing-masing object sebagai dictionary
print(f"Atribut object1 = {object1.__dict__}")
print(f"Atribut object2 = {object2.__dict__}")

# Print atribut nama
print(f"Nama object1 = {object1.nama}")
print(f"Nama object2 = {object2.nama}")