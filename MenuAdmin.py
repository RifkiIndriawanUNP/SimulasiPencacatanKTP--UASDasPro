import TambahKTP
import UpdateKTP
import LihatKTP
import LihatLaporan

def menu_admin():
    while True:
        print("\n=== MENU ADMIN ===")
        print("1. Tambah Data KTP")
        print("2. Update Data KTP")
        print("3. Lihat Data KTP")
        print("4. Lihat Laporan Warga")
        print("5. Kembali")
        
        pilihan = input("Pilih menu (1-4): ")
        
        if pilihan == "1":
            TambahKTP.tambah_ktp()
        elif pilihan == "2":
            UpdateKTP.updateKtp()
        elif pilihan == "3":
            LihatKTP.lihat_ktp()
        elif pilihan == "4":
            LihatLaporan.lihat_laporan()
        elif pilihan == "5":
            break
        else:
            print("Pilihan tidak valid!")