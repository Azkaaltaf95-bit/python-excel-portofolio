nama = input("Masukan Nama : ")
nilai = int(input("Maukan Nilai : "))

if nilai>=68:
    status = "Anda Lulus"
else:
    status = "Anda Tidak Lulus"

print("Nama :",nama)
print("Nilai :",nilai)
print("Status :",status)