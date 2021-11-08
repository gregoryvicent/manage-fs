from os import getcwd, listdir, path
from colorama import Fore, Style


dirs = getcwd().split("/")
path_now = "/".join(dirs)


def print_path():
    return path_now


def open_dir(number_dir):
    try:
        global path_now

        list_dir = listdir(path_now)
        new_dir = list_dir[number_dir]

        if not path.isdir(f"{path_now}/{new_dir}"):
            raise NotADirectoryError()

        dirs.append(new_dir)

        path_now = '/'.join(dirs)

    except NotADirectoryError:
        print()
        print(Fore.RED + "-------- El elemento seleccionado no es un Directorio")
        print()


def exit_dir():
    global path_now

    dirs.pop()

    path_now = '/'.join(dirs)


def show_this_dir():
    list_dir = listdir(path_now)

    for elements in list_dir:
        if path.isdir(path_now + "/" + elements):
            print(list_dir.index(elements), Fore.RED + elements, "(D)")
        elif path.isfile(path_now + "/" + elements):
            print(list_dir.index(elements), Fore.LIGHTBLUE_EX + elements, "(F)")
        else:
            print(list_dir.index(elements), Fore.WHITE + elements, "(Not)")

    print()
    print(Fore.YELLOW + Style.BRIGHT +
          f"------- Directorio Actual: {path_now}")
    print()
