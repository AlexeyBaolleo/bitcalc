import argparse
import sys
import os

def parse_input(user_input: str) -> int:
    user_input = user_input.strip().lower()
    if user_input[:2] == "0x":
        return int(user_input[2:], 16)
    elif user_input[:2] == "0b":
        return int(user_input[2:], 2)
    elif user_input.isdigit():
        return int(user_input)
    else:
        raise ValueError("Не поддерживаемый формат числа")


def convert(user_input: str) -> str:
    try:
        number = parse_input(user_input)
        return (
            f"DEC: {number}\n"
            f"BIN: {bin(number)}\n"
            f"HEX: {hex(number)}\n"
        )
    except ValueError as e:
        return e


def format_output(res: int) -> int:
    return f"DEC: {res}, BIN: 0b{res:04b}"


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


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_welcome():
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

def run_ui():
    clear_console()
    print_welcome()


    print("")



def main():
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

    parsed = parser.parse_args()

    if not parsed.func:
        run_ui()
        return

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

if __name__ == "__main__":
    main()

    # ------------------ ЗАДАЧИ НА ЗАВТРА, УТРО------------------------
    # доделать для отрицательных чисел
    # Добавить гит + README.md
    # Добавить минимальный UI (Введите число, введите операцию и т.п.)