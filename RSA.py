def rsa_encrypt(pesan, e, n):
    # Konversi pesan ke daftar bilangan bulat menggunakan nilai Unicode
    pesan_int = [ord(karakter) for karakter in pesan]
    
    # Enkripsi setiap bilangan bulat menggunakan rumus (enkripsi = karakter^e mod n) dan simpan dalam bentuk daftar
    chipertext = [pow(karakter, e, n) for karakter in pesan_int]
    
    # Konversi daftar bilangan bulat dalam bentuk pesan terenkripsi berupa string tunggal
    pesan_terenkripsi = "_".join(map(str, chipertext))
    
    return pesan_terenkripsi

def rsa_decrypt(pesan_terenkripsi, d, n):
    # Konversi string pesan terenkripsi menjadi daftar bilangan bulat
    pesan_terenkripsi = [int(bagian) for bagian in pesan_terenkripsi.split("_")]
    
    # Dekripsi setiap bilangan bulat menggunakan rumus (deskripsi = karakter^d mod n) dan simpan dalam bentuk daftar
    pesan_int = [pow(karakter, d, n) for karakter in pesan_terenkripsi]
    
    # Konversi daftar bilangan bulat dalam bentuk pesan dalam bentuk string
    pesan_terdekripsi = "".join([chr(karakter) for karakter in pesan_int])
    
    return pesan_terdekripsi

# Inisiasi variabel yang diperlukan
p = 23
q = 41
n = p * q  # kunci publik
phi = (p - 1) * (q - 1)
e = 7  # kunci publik
d = pow(e, -1, phi)  # kunci privat

pesan_asli = "MUHAMMAD HAIKAL FIKRI ASAD"

pesan_terenkripsi = rsa_encrypt(pesan_asli, e, n)
pesan_terdekripsi = rsa_decrypt(pesan_terenkripsi, d, n)

# chiper = pow(65,7,943)
# print("hasil dari rumus eknkripsi : ",chiper)
print("Pesan asli:", pesan_asli)
print("Pesan terenkripsi:", pesan_terenkripsi)
print("Pesan terdekripsi:", pesan_terdekripsi)
