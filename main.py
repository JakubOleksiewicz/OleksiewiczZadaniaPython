import os


def clear_console():
    os.system("cls" if os.name == "nt" else "clear")


def calculator_program():
    print("Kalkulator placeholder")


def temperature_program():
    print("Temperature placeholder")


def arithmetic_program():
    print("Arithmetic placeholder")


def display_menu():
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("Wybierz program do uruchomienia:")
    print("0. WYJŚCIE")
    print("1. Kalkulator")
    print("2. Konwerter temperatur")
    print("3. Średnia ocen")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    return input("Wybierz opcję: ")


def main():
    flag = True
    while flag:
        clear_console()
        choice = display_menu()
        if choice == "0":
            flag = False
            clear_console()
            print("Wyłączono program")
        elif choice == "1":
            calculator_program()
        elif choice == "2":
            temperature_program()
        elif choice == "3":
            arithmetic_program()


if __name__ == "__main__":
    main()
