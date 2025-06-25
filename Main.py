import MenuAdmin
import MenuUser

DATA_LOGIN = {
    "admin": "admin123",
    "user": "password"
}

while True:
    print("===Aplikasi Pencatatan KTP===\n")
    print("=== LOGIN ===")
    username = input("Username: ")
    password = input("Password: ")
        
    if username == 'admin':
        if username in DATA_LOGIN and DATA_LOGIN[username] == password:
            print(f"Login berhasil")
        MenuAdmin.menu_admin()
    elif username == 'user':
        if username in DATA_LOGIN and DATA_LOGIN[username] == password:
            print(f"Login berhasil")
        MenuUser.menu_user()
    else:
        print("===Username atau password salah===")
    