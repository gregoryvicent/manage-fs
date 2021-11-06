from os import getcwd, listdir, path
from colorama import Fore, Style


dirs = getcwd().split("/")
path_now = "/".join(dirs)


def open_dir(number_dir):
    global path_now

    list_dir = listdir(path_now)
    new_dir = list_dir[number_dir]

    dirs.append(new_dir)

    path_now = '/'.join(dirs)


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
    print(Fore.YELLOW + Style.BRIGHT + f"------- Directorio Actual: {path_now}")
    print()