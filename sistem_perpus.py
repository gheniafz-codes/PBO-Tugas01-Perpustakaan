class Buku:
    def __init__(self, judul, penulis, stok):
        self.judul = judul
        self.penulis = penulis
        self.stok = stok
    
    def info_buku(self): #INFO MENAMPILKAN DAFTAR BUKU
        print(f"JUDUL: {self.judul} | PENULIS: {self.penulis} | STOK: {self.stok}")

#STOK BUKU BERUBAH SAAT ADA PROSES PINJAM DAN KEMBALIKAN
    def pinjam(self): 
        if self.stok > 0:
            self.stok -= 1
            return True
        else:
            print(f"Maaf, stok buku '{self.judul}' sedang kosong.")
            return False

    def kembalikan(self):
        self.stok += 1


class Anggota:
    def __init__(self, nama, nim, kode_member):
        self.nama = nama
        self.nim = nim
        self.kode_member = kode_member
        self.buku_dipinjam = [] # List kosong untuk menyimpan buku yg dipinjam anggota

    def tampilkan_profil(self): #menampilkan profil awal anggota
        print(f"\n===== Profil Anggota =====")
        print(f"Nama: {self.nama}")
        print(f"Nim: {self.nim}")
        print(f"Kode Member: {self.kode_member}")

        if len(self.buku_dipinjam) > 0:
            print(f"Total Buku Dipinjam: {len(self.buku_dipinjam)}")
            judul_buku = [b.judul for b in self.buku_dipinjam] 
            print(f"Daftar Buku: {', '.join(judul_buku)}") 
        else:
            print("Tidak ada buku yang sedang dipinjam.")

#MEMASUKKAN BUKU YANG DIPINJAM/ DIKEMBALIKAN KE LIST self.buku_dipinjam = [] DI PROFIL
    def pinjam_buku(self, buku): 
        self.buku_dipinjam.append(buku)

    def kembalikan_buku(self, buku):
        if buku in self.buku_dipinjam:
            self.buku_dipinjam.remove(buku)


class Perpustakaan:
    def __init__(self, perpus_uin):
        self.perpus_uin = perpus_uin
        self.daftar_buku = []
        self.daftar_anggota = []

    def tambah_buku(self, buku): #sistem menambah buku ke daftar buku
        self.daftar_buku.append(buku)
        print(f"[Sistem] Buku '{buku.judul}' berhasil ditambahkan.")

    def registrasi_anggota(self, anggota): #sistem menambahkan anggota ke daftar anggota
        self.daftar_anggota.append(anggota)
        print(f"[Sistem] Anggota '{anggota.nama}' berhasil didaftarkan.")

#INTERAKSI ANTAR OBJEK (ANGGGOTA DAN BUKU)
    def proses_peminjaman(self, anggota, buku): #sistem mengatur peminjaman buku
        print(f"\n[Proses] {anggota.nama} ingin meminjam '{buku.judul}'...")
        
        # Cek stok buku
        if buku.pinjam(): 
            anggota.pinjam_buku(buku)
            print(">> Peminjaman BERHASIL!")
        else:
            print(">> Peminjaman GAGAL!")

    def proses_pengembalian(self, anggota, buku): #sistem mengatur pengembalian buku
        print(f"\n[Proses] {anggota.nama} mengembalikan '{buku.judul}'...")
        buku.kembalikan()
        anggota.kembalikan_buku(buku)
        print(">> Pengembalian BERHASIL!")