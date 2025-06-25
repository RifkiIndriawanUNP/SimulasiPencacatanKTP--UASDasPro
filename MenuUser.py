import LihatKTP
import Laporan

def menu_user():
    while True:
        print("\n=== MENU USER ===")
        print("1. Lihat Data KTP")
        print("2. Laporkan Kesalahan")
        print("3. Kembali")
        
        pilihan = input("Pilih menu (1-3): ")
        
        if pilihan == "1":
            LihatKTP.lihat_ktp()
        elif pilihan == "2":
            Laporan.lapor_kesalahan()
        elif pilihan == "3":
            break
        else:
            print("Pilihan tidak valid!")