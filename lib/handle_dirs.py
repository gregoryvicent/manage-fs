from os import mkdir, rmdir, remove, path, listdir
from colorama import Fore

from lib.browser import print_path


def create_dir():
    new_element = input("Nombre del elemento a crear: ")
    final_address = f"{print_path()}/{new_element}"

    if new_element[-1] == "/":
        mkdir(final_address)
    else:
        file = open(final_address, "w")
        file.close()


def delete_dir():
    element_remove = int(input("Número del elemento a eliminar: "))
    dir_elements = listdir(print_path())
    element = dir_elements[element_remove]
    final_address = f"{print_path()}/{element}"


    if path.isdir(final_address):
        rmdir(final_address)
    elif path.isfile(final_address):
        remove(final_address)
    else:
        print(Fore.RED + "---------- Elemento seleccionado no valido.")
