import os


def clear_console():
    os.system("cls" if os.name == "nt" else "clear")


def int_validation():
    while True:
        try:
            return int(input())
        except:
            print("Wprowadź poprawną liczbę: ", end="")


def float_validation():
    while True:
        try:
            value = input().replace(",", ".")
            return float(value)
        except:
            print("Wprowadź poprawną liczbę: ", end="")


def calculator_program():
    clear_console()
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

    while True:
        operation = input("Wybierz operację [+, -, *, /]: ")
        if operation in ["+", "-", "*", "/"]:
            break
        else:
            print("Wybierz poprawną operację")

    print("Podaj liczbę a: ", end="")
    a = float_validation()
    print("Podaj liczbę b: ", end="")
    b = float_validation()

    if operation == "+":
        print(f"{a} + {b} = {a + b}")
    elif operation == "-":
        print(f"{a} - {b} = {a - b}")
    elif operation == "*":
        print(f"{a} * {b} = {a * b}")
    elif operation == "/":
        if b == 0:
            print("Nie można dzielić przez 0")
        else:
            print(f"{a} / {b} = {a / b}")

    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    input("Naciśnij ENTER aby wrócić do menu")


def temperature_program():
    clear_console()
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

    print("Kierunki konwersji:")
    print("C - Celsjusze na Fahrenheity")
    print("F - Fahrenheity na Celsjusze")
    while True:
        operation = input("Wybierz operację kierunek: ")
        if operation in ["C", "F"]:
            break
        else:
            print("Podano błędną opcję")

    print(f"Podaj liczbę w °{operation}: ", end="")
    degree = float_validation()
    if operation == "C":
        print(f"{degree}°C = {degree * 1.8 + 32}°F")
    elif operation == "F":
        print(f"{degree}°F = {(degree - 32) / 1.8}°C")

    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    input("Naciśnij ENTER aby wrócić do menu")


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
