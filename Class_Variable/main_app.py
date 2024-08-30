class Friends():

    jumlah_friend = 0 # ini adalah class variable, variable yg nempel di class
    
    def __init__(self, InputNama, InputKota, InpitKelamin) -> None:
        self.nama = InputNama       # Ini adalah atribut, variable yg nempel di object
        self.kota = InputKota
        self.kelamin = InpitKelamin
        Friends.jumlah_friend += 1  # Salah satu kegunaannya untuk mengecek jumlah object dari class
        print(f"Membuat Object dengan nama : {InputNama}")
        print(f"Jumlah Object saat ini = {Friends.jumlah_friend}")


friend1 = Friends("Otong", "Jakarta", "Laki-laki")
friend2 = Friends("Odah", "Bogor", "Perempuan")
print("\n")
print(f"friend1 namanya {friend1.nama} seorang {friend1.kelamin}, asalnya dari {friend1.kota}")
print(f"friend2 namanya {friend2.nama} seorang {friend2.kelamin}, asalnya dari {friend2.kota}")
print(f"\nJumlah Friends saat ini adalah {Friends.jumlah_friend}, yaitu {friend1.nama} dan {friend2.nama}")