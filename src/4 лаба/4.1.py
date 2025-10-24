from pathlib import Path
import csv


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    '''
    Открывает текстовый файл и возвращает его содержимое как одну строку.

    По умолчанию используется кодировка UTF-8.
    При необходимости можно указать другую, например encoding="cp1251".
    '''
    path = Path(path)
    with path.open('r', encoding=encoding) as file:
        return file.read()  


def ensure_parent_dir(path: str | Path) -> None:
    '''
    Создаёт родительские директории для указанного пути, если их нет.

    Полезно перед записью файла, чтобы избежать ошибки FileNotFoundError.
    '''
    path = Path(path)
    parent = path.parent
    if not parent.exists():
        parent.mkdir(parents=True, exist_ok=True)


def write_csv(rows: list[tuple | list], path: str | Path, header: tuple[str, ...] | None = None) -> None:
    '''
    Создаёт или перезаписывает CSV-файл с разделителем ','.

    Если указан header, записывает его первой строкой.
    Проверяет, что все строки в 'rows' имеют одинаковую длину.
    '''
    if not rows:
        raise ValueError("Список строк 'rows' не может быть пустым.")

    row_lengths = {len(r) for r in rows}
    if len(row_lengths) > 1:
        raise ValueError("Все строки в 'rows' должны быть одинаковой длины.")

    ensure_parent_dir(path)

    path = Path(path)
    with path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=",")
        if header:
            writer.writerow(header)
        writer.writerows(rows)


input_path = Path("data/input.txt")

try:
    content = read_text(input_path, encoding="utf-8")
    print("Содержимое файла input.txt:\n", content)
except FileNotFoundError:
    print("Файл не найден!")
except UnicodeDecodeError:
    print("Ошибка кодировки! Попробуйте encoding='cp1251'.")


rows = [
    (1, 'Петя', 17),
    (2, 'Ваня', 18),
    (3, 'Егор', 17)
]
write_csv(rows, "output/users.csv", header=("ID", "Name", "Age"))

print("\n Файл 'output/users.csv' успешно создан!")