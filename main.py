import argparse
import sys
import os


def parse_input(user_input: str) -> int:
    user_input = user_input.strip().lower()
    
    is_negative = False
    if user_input[0] == "-":
        user_input = user_input[1:]
        is_negative = True

    if user_input[:2] == "0x":
        number = int(user_input[2:], 16)
    elif user_input[:2] == "0b":
        number = int(user_input[2:], 2)
    elif user_input.isdigit():
        number = int(user_input)
    else:
        raise ValueError("Не поддерживаемый формат числа")

    return -number if is_negative else number

def convert(user_input: str) -> str:
    try:
        number = parse_input(user_input)
        return (
            f"DEC: {number}\n"
            f"BIN: {bin(number)}\n"
            f"HEX: {hex(number)}\n"
        )
    except ValueError as e:
        return str(e)


def format_output(res: int) -> int:
    if res < 0:
        return f"DEC: {res}, BIN: -0b{abs(res):b}, HEX: -0x{abs(res):x}"
    return f"DEC: {res}, BIN: 0b{res:b}, HEX: 0x{res:x}"


def logical_AND(a: int, b: int) -> str:
    res = a & b
    return format_output(res)


def logical_OR(a: int, b: int) -> str:
    res = a | b
    return format_output(res)


def logical_XOR(a: int, b: int) -> str:
    res = a ^ b
    return format_output(res)


def logical_NOT(a: int) -> str:
    res = ~a
    return format_output(res)


def shift_left(a: int, length: int) -> str:
    res = a << length
    return format_output(res)


def shift_right(a: int, length: int) -> str:
    res = a >> length
    return format_output(res)


def clear_console() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')

def print_welcome() -> None:
    border = '═' * 40
    italic_mildy = r'''
  __  __   _   _       _         
 |  \/  | (_) | |     | |        
 | \  / |  _  | |   __| |  _   _ 
 | |\/| | | | | |  / _` | | | | |
 | |  | | | | | | | (_| | | |_| |
 |_|  |_| |_| |_|  \__,_|  \__, |
                            __/ |
                           |___/ 
'''
    
    print("╔" + border + "╗")
    print("║{:^40}║".format("Добро пожаловать в"))
    print("║{:^40}║".format(""))
    for line in italic_mildy.splitlines():
        print("║{:^40}║".format(line))
    print("║{:^40}║".format(""))
    print("╚" + border + "╝")

def run_ui() -> None:
    clear_console()
    print_welcome()


    print (
        "1) convert - конвертирует число в десятичное/двоичное/шестнадцетиричное,\n"
        "2) and - Логическое И,\n"
        "3) or - Логическое ИЛИ,\n"
        "4) xor - Исключающее ИЛИ,\n"
        "5) not - Логическое НЕ,\n"
        "6) shl - Сдвиг влево на N,\n"
        "7) shr - Сдвиг вправо на N,\n" )

    answer = ""
    while True:
        answer = input("Введите нужную функцию или введите exit для выхода: ")

        if answer == "1":
            print("Введите число для конвертации в любой системе счисления (двоичной, десятичной, шестнадцетиричной)")
            try:
                a = input("Введите число: ")
                print(convert(a))
            except Exception as e:
                print(e)
            
        elif answer == "2":
            print("Введите два числа для выполнения логической операции И, AND( & )")
            try:
                a = int(input("Введите первое число: "), 0)
                b = int(input("Введите второе число: "), 0)
                print(logical_AND(a, b))
            except ValueError:
                print(f"Не поддерживаемый формат числа, введите число (0b1010, 10, 0xA)")

        elif answer == "3":
            print("Введите два числа для выполнения логической операции ИЛИ, OR( | )")
            try:
                a = int(input("Введите первое число: "), 0)
                b = int(input("Введите второе число: "), 0)
                print(logical_OR(a, b))
            except ValueError:
                print(f"Не поддерживаемый формат числа, введите число (0b1010, 10, 0xA)")
        elif answer == "4":
            print("Введите два числа для выполнения логической операции Исключающие ИЛИ, XOR( ^ )")
            try:
                a = int(input("Введите первое число: "), 0)
                b = int(input("Введите второе число: "), 0)
                print(logical_XOR(a, b))
            except ValueError:
                print(f"Не поддерживаемый формат числа, введите число (0b1010, 10, 0xA)")
        elif answer == "5":
            print("Введите число для выполнения логической операции НЕ, NOT( ~ )")
            try:
                a = int(input("Введите число: "), 0)
                print(logical_NOT(a))
            except ValueError:
                print(f"Не поддерживаемый формат числа, введите число (0b1010, 10, 0xA)")
        elif answer == "6":
            print("Введите число и длину для выполнения сдвига влево ( << )")
            try:
                a = int(input("Введите число: "), 0)
                length = int(input("Ввдите длину сдвига: "), 0)
                print(shift_left(a, length))
            except ValueError:
                print(f"Не поддерживаемый формат числа, введите число (0b1010, 10, 0xA)")
        elif answer == "7":
            print("Введите число и длину для выполнения сдвига вправо ( >> )")
            try:
                a = int(input("Введите число: "), 0)
                length = int(input("Ввдите длину сдвига: "), 0)
                print(shift_right(a, length))
            except ValueError:
                print(f"Не поддерживаемый формат числа, введите число (0b1010, 10, 0xA)")
        elif answer == "exit":
            break
        else:
            print("Нет такой функции")


def main() -> None:
    FUNCTIONS = {
        "convert": convert,
        "and": logical_AND,
        "or": logical_OR,
        "xor": logical_XOR,
        "not": logical_NOT,
        "shl": shift_left,
        "shr": shift_right
    }

    ARG_COUNTS = {
        "convert": 1,
        "and": 2,
        "or": 2,
        "xor": 2,
        "not": 1,
        "shl": 2,
        "shr": 2
    }


    parser = argparse.ArgumentParser()
    parser.add_argument("func", nargs="?",
                            help="""convert - конвертирует число в десятичное/двоичное/шестнадцетиричное,
                            and - Логическое И,
                            or - Логическое ИЛИ,
                            xor - Исключающее ИЛИ,
                            not - Логическое НЕ,
                            shl - Сдвиг влево на N,
                            shr - Сдвиг вправо на N,""")
    parser.add_argument("args", nargs=argparse.REMAINDER, 
                            help="""and: A & B
                            or: А | B
                            xor: A ^ B
                            not: ~A
                            shl: A << Length
                            shr: A >> Length""")

    parser.add_argument("--output", help="Путь к файлу для вывода результата")

    parsed = parser.parse_args()

    if not parsed.func:
        try:
            run_ui()
        except KeyboardInterrupt:
            print("\nВыход")


    if parsed.func not in FUNCTIONS:
        print("Нет такой функции.")
        sys.exit(1)
        
    expected = ARG_COUNTS[parsed.func]
    if len(parsed.args) != expected:
        print(f"Функция '{parsed.func}' ожидает {expected} аргументов, получено {len(parsed.args)}.")
        sys.exit(2)

    try:
        if parsed.func == "convert":
            print(FUNCTIONS[parsed.func](*parsed.args))
        else:
            parsed_args = [parse_input(args) for args in parsed.args]
            print(FUNCTIONS[parsed.func](*parsed_args))
    except TypeError as e:
        print(f"Неверные аргументы для {parsed.func}: {e}")
        sys.exit(3)
    except ValueError as e:
        print(f"Ошибка {e}")
        sys.exit(4)

    if parsed.output:
        with open(parsed.output, "w") as f:
            f.write(result + "\n")
    else:
        print(result)


if __name__ == "__main__":
    main()
