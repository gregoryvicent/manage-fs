from colorama import Fore

from lib.browser import show_this_dir, open_dir, exit_dir
from lib.handle_dirs import create_dir, delete_dir


def choose_option():
    get_action = input("Indique la acción que quiere realizar: ")
    if get_action == "1":
        get_number_dir = int(input("Número del directorio: "))

        open_dir(get_number_dir)
        show_interface()
    elif get_action == "2":
        exit_dir()
        show_interface()
    elif get_action == "3":
        create_dir()
        show_interface()
    elif get_action == "4":
        delete_dir()
        show_interface() 
    else:
        print()
        print(Fore.RED + "¡¡¡¡¡Opcion no valida!!!!!")

        show_interface()


def show_interface():
    print()
    print("------------- Elementos del Directorio -------------")
    print()

    show_this_dir()

    print("""
  1- Entrar    2- Salir   3- Crear    4- Eliminar 
          """)

    choose_option()
