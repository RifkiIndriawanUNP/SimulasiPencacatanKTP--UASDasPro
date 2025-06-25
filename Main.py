import Login

def Utama():
    while True:
        print("\n=== Aplikasi Pencatatan Data KTP ===")
        print("1. Login\n2. Keluar")
        menu = input("pilih menu (1-2): ")
        if menu == '1':
            Login.Login()
        elif menu == '2':
            break
        else:
            print("Pilihan tidak valid!") 
    
if __name__ == "__main__":
  Utama()