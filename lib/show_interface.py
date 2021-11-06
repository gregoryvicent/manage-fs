from lib.handle_path import show_this_dir, open_dir, exit_dir


def choose_option():
    get_action = input("Indique la acción que quiere realizar: ")
    if get_action == "1":
        get_number_dir = int(input("Número del directorio: "))

        open_dir(get_number_dir)
        show_interface()
    elif get_action == "2":
        exit_dir()
        show_interface()
    else:
        print("¡¡¡¡¡Opcion no valida!!!!!")
        show_interface()


def show_interface():
    print()
    print("------------- Elementos del Directorio -------------")
    print()

    show_this_dir()

    print("""
  1- Enter dir.    2- Exit dir.
          """)

    choose_option()
