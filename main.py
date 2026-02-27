from entities.user import User
from getpass import getpass

def register_user():
    name = input("Nombre: ")
    account = input("Cuenta: ")

    if User.check_account_exists(account):
        print("La cuenta ya existe")
    else:
        curp = input("CURP: ")
        password = getpass("Contraseña: ")
        User.insert(name, curp, account, password)

def views_users():
    users = User.get_users()
    for user in users:
        print (f"------------------------------")
        print(f"Nombre: {user.name}, CURP: {user.curp}, Cuenta: {user.account}, Contraseña: {user.password}")

def login():
    account = input("Cuenta: ")
    password = getpass("Contraseña: ")

    user = User.get_user_by_account(account)
    if user and user.password == password:
        return True
    else:
        return False


if __name__ == "__main__":
    print("Inicio de sesión")
    # Validar si la cuenta existe antes de pedir contraseña
   
    if login():
        print("Seleccione una operacion del menu")
        print("1.- Registrar un usuario")
        print("2.- Consultar usuarios")
        option = int(input())
        if option == 1:
            register_user()
        elif option == 2:
            views_users()

    else:
        print("Credenciales invalidas")