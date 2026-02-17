from sistem_perpus import Buku,Anggota,Perpustakaan

# SISTEM PERPUSTAKAAN 
perpus_uin = Perpustakaan("Perpustakaan UIN Suska")
print('PERPUSTAKAAN UIN SUSKA')

# BUAT OBJEK BUKU
buku1 = Buku("Pemrograman Python (001)", "Guido van Rossum", 4)
buku2 = Buku("Kalkulus Dasar (002)", "James Stewart", 5)
buku3 = Buku("Sistem Basis Data (003)", "Fathansyah", 7)

# DAFTARKAN OBJEK BUKU KE SISTEM
perpus_uin.tambah_buku(buku1)
perpus_uin.tambah_buku(buku2)
perpus_uin.tambah_buku(buku3)

# BUAT OBJEK ANGGOTA
anggota1 = Anggota("Ghenia", "1234567890")
anggota2 = Anggota("Zahra", "098765421")

# DAFTARKAN OBJEK ANGGOTA KE SISTEM
perpus_uin.registrasi_anggota(anggota1)
perpus_uin.registrasi_anggota(anggota2)

# CEK INFO AWAL
# buku
print(f"\n===== DAFTAR BUKU =====")
buku1.info_buku()
buku2.info_buku()
buku3.info_buku()
# anggota
anggota1.tampilkan_profil()
anggota2.tampilkan_profil()

# SKENARIO PEMINJAMAN
perpus_uin.proses_peminjaman(anggota1, buku1)
perpus_uin.proses_peminjaman(anggota1, buku2)
perpus_uin.proses_peminjaman(anggota2, buku3)

# CEK INFO SETELAH PEMINJAMAN
# buku
print(f"\n===== DAFTAR BUKU =====")
buku1.info_buku()
buku2.info_buku()
buku3.info_buku()
# anggota
anggota1.tampilkan_profil()
anggota2.tampilkan_profil()

# SKENARIO PENGEMBALIAN
perpus_uin.proses_pengembalian(anggota1, buku1)
perpus_uin.proses_pengembalian(anggota2, buku3)

# CEK INFO SETELAH PENGEMBALIAN
# buku
print(f"\n===== DAFTAR BUKU =====")
buku1.info_buku()
buku2.info_buku()
buku3.info_buku()
# anggota
anggota1.tampilkan_profil()
anggota2.tampilkan_profil()