import Login

while True:
    print("=== Aplikasi Pencatatan Data KTP ===")
    print("\n1. Login\n2. Keluar")
    menu = input("pilih menu (1-2): ")
    if menu == '1':
        Login.Login()
    elif menu == '2':
        break
    else:
        print("Pilihan tidak valid!") 
    