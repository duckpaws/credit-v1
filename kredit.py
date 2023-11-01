# Input dari pengguna
pinjaman_pokok = float(input("Masukkan jumlah pinjaman (IDR): "))
tingkat_bunga_tahunan = float(input("Masukkan tingkat bunga tahunan (%): "))
jangka_waktu_bulan = int(input("Masukkan jangka waktu pinjaman (bulan): "))

# Menghitung tingkat bunga bulanan
tingkat_bunga_bulanan = tingkat_bunga_tahunan / 12 / 100

# Menghitung jumlah pembayaran bulanan
pembayaran_bulanan = (pinjaman_pokok * tingkat_bunga_bulanan) / (1 - (1 + tingkat_bunga_bulanan) ** -jangka_waktu_bulan)

# Menampilkan hasil
print(f"Jumlah pembayaran bulanan adalah: IDR {pembayaran_bulanan:.2f}")
