# Inisialiasi Kelas Friends
class Friends():
    pass

# Inisialisasi Object friend1 ke dalam kelas Friends
friend1 = Friends()

# Inisiasi Atribut Object, dimana friend punya nama, kota dan kelamin
friend1.nama = "Samsul"
friend1.kota = "Jakarta"
friend1.kelamin = "Laki-laki"

# Membuktikan bahwa friend adalah object
print(f"Ini adalah friend1 = {friend1}")

# Print atribut friend
print(f"Ini adalah atribut friend1 = {friend1.__dict__}")

# Print nama friend1
print(f"Nama friend1 adalah = {friend1.nama}")

# Print kota friend1
print(f"Kota friend1 adalah = {friend1.kota}")

# Print kelamin friend1
print(f"Kelamin friend1 adalah = {friend1.kelamin}")