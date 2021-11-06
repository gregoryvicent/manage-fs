from lib.show_interface import show_interface
from colorama import Fore, init


def run():
    init(autoreset=True)

    try:
        show_interface()
    except KeyboardInterrupt:
        print()
        print(Fore.CYAN + "\n------- Se a cerrado el programa. Hasta luego :3 -------")


if __name__ == "__main__":
    run()
