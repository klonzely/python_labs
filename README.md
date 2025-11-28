# python_labs

# Лабораторная работа 2
## Задание 1.1
![скриншот задания 1](/scr/2%20лаба/img/1..1.png)
        nums = [1.5, 2, 2.0, -3.1]
            def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
                if nums:
                    return min(nums), max(nums)
                else:
                    return 'ValueError'
            print(min_max(nums))
## Задание 1.2
![скриншот задания 1](/scr/2%20лаба/img/1.2.png)
    m =[3, 1, 2, 1, 3]
    def unique_sorted(nums: list[float | int]) -> list[float | int]:
        return sorted(set(m))
    print(unique_sorted(m))
## Задание 1.3
![скриншот задания 1](/scr/2%20лаба/img/1.3.png)
    mat = [[1, 2], [3, 4]]
    def flatten(mat: list[list | tuple]) -> list:
        if all(type(x) == list or type(x) == tuple for x in mat):
            return [mat[i][j] for i in range(len(mat)) for j in range(len(mat[i]))]
        else:
            return 'TypeError'
    print(flatten(mat))
## Задание 2.1
![скриншот задания 2](/scr/2%20лаба/2.1.py)
    mat=[[1, 2, 3]]
    def transpose(mat: list[list[float | int]]) -> list[list]:
        if len(mat)==0:
            return []
        for i in range (len(mat)-1):
            if len(mat[i])!=len(mat[i+1]):
                return ValueError
        transp = []
        for col_index in range(len(mat[0])):
            row_new = []
            for row_index in range(len(mat)):
                row_new.append(mat[row_index][col_index])
            transp.append(row_new)
        return transp
    print(transpose(mat))
## Задание 2.2
![скриншот задания 2](/scr/2%20лаба/img/2.2.png)
    mat =[[1, 2], [3]]
    def row_sums(mat: list[list[float | int]]) -> list[float]:
        for i in range (len(mat)-1):
            if len(mat[i])!=len(mat[i+1]):
                return 'ValueError'
        a=[]
        for i in range (len(mat)):
            a.append(sum(mat[i]))
        return a
    print(row_sums(mat))
## Задание 2.3
![скриншот задания 2](/scr/2%20лаба/img/2.3.png) 
    mat = [[1, 2], [3]]
    def col_sums(mat: list[list[float | int]]) -> list[float]:
        for i in range (len(mat)-1):
            if len(mat[i])!=len(mat[i+1]):
                return 'ValueError'
        if not mat:
            return []
        res = []
        for i in range(len(mat[0])):
            res.append(sum(mat[j][i] for j in range(len(mat))))
        return res
    print(col_sums(mat))
 ## Задание 3
![скриншот задания 3](/scr/2%20лаба/img/3..png)
    inp = ('иванов иван иванович', 'BIVT-25', 4.6)
    def format_record(rec: tuple[str, str, float]) -> str:
        """Некорректные записи -> ValueError"""
        fio, group, gpa = inp[0], inp[1], inp[2]
        if fio == '' or group == '' or type(gpa) != float:
            return 'ValueError'
        fio = fio.split()
        for i in range(len(fio)):
            fio[i] = fio[i][0].upper() + fio[i][1:]
        return f'{fio[0]} {fio[1][0]}.{fio[2][0]}., гр. {group}, GPA {gpa:.2f}'
    print(format_record(inp)) 


# Лабораторная работа 3
## Задание 1.1
```python
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    # замена управляющих символов на пробелы
    control_character = ['\n', '\t', '\r']
    for char in control_character:
        text = text.replace(char, ' ')
      # удаление лишних пробелов
    words = text.split()
    text = ' '.join(words)

    if yo2e:
        text = text.replace('ё', 'е').replace('Ё', 'Е')

    if casefold:
        text = text.casefold()
    
    return text
```

![скриншот задания 1](/src/3%20лаба/img/image.png)
## Задание 1.2
![скриншот задания 1](/scr/3%20лаба/img/3.2.png)




# Лабораторная работа 4
## Задание 1.1
```python
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
```
![скриншот задания 1](/src/4%20лаба/img/4.1.png)

## Задание 1.2
```python
    import sys
    import os
    sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
    from src.text import tokenize, count_freg, top_n, normalize
    import csv
    from pathlib import Path

    table = True

    def print_table(top: list[tuple]):
        """
        Выводит топ слов с их частотами в табличном формате.

        Форматирует таблицу с двумя столбцами: слово и частота.
        Ширина столбца "слово" подстраивается под максимальную длину слова из списка.

        """
        if not top:
            print('Нет слов для отображения')
            return
        max_len = max(len(word) for word, _ in top)
        col_word = 'слово'
        col_freq = 'частота'

        width_word = max(max_len, len(col_word))
        width_freq = len(col_freq)
        print(f"{col_word:<{width_word}} | {col_freq}")
        print("-" * width_word + "-+-" + "-" * width_freq)

        for word, count in top:
            print(f"{word:<{width_word}} | {count}")


    def main():
        input_path = Path('data/input.txt')     # путь к входному файлу 
        output_path = Path("data/report.csv")   # путь куда нужно сохранить отчёт

        if not input_path.exists():
            print(f"Файл {input_path} не найден!")
            sys.exit(1)

        try:
            text = input_path.read_text(encoding="utf-8")
        except UnicodeDecodeError as e:
            print(f"Ошибка кодировки при чтении {input_path}: {e}")
            sys.exit(1) # принудительно завершаем программу 

        text = normalize(text)
        tokens = tokenize(text)
        freq = count_freg(tokens)

        def sort_key(item):
            '''
            функция сортировки по частоте 
            '''
            word, count = item
            return (-count, word)

        sorted_items = sorted(freq.items(), key=sort_key)
        
        # создание папки и запись csv
        output_path.parent.mkdir(parents=True, exist_ok=True)  # создаём все недостающие папки
        with output_path.open("w", newline="", encoding="utf-8") as file: # открывает csv файл для записи
            writer = csv.writer(file) # создаёт объект, который умеет писать CSV-строки
            writer.writerow(["word", "count"]) # записывает заголовок таблицы.
            writer.writerows(sorted_items) # записывает все пары (слово, количество
        
        # статистика по тексту 
        total_words = sum(freq.values())
        unique_words = len(freq)
        top5 = top_n(freq, n=5)

        print(f"Всего слов: {total_words}")
        print(f"Уникальных слов: {unique_words}")
        print(f"Топ: {top5}")

        if table:
            print("\nТаблица топ слов:")
            print_table(top5)

    if name == "__main__":
        main()
```
![скриншот задания 2](/src/4%20лаба/img/4.2.png)


# Лабораторная работа 5
## Задание 1.1
```python
import csv
from pathlib import Path
try:
    from openpyxl import Workbook
except ImportError:
    raise ImportError("Для работы модуля требуется установить openpyxl: pip install openpyxl")


def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    """
    Конвертирует CSV в XLSX.
    Использовать openpyxl.
    Первая строка CSV — заголовок.
    Лист называется "Sheet1".
    Колонки — автоширина по длине текста (не менее 8 символов).
    """
    csv_file = Path(csv_path)
    if not csv_file.exists():
        raise FileNotFoundError(f"CSV файл не найден: {csv_path}")
    
    if not csv_file.suffix.lower() == '.csv':
        raise ValueError(f"Неверный тип файла: ожидается .csv, получен {csv_file.suffix}")
    
    try:
        with csv_file.open('r', encoding='utf-8') as f:
            reader = csv.reader(f)
            rows = list(reader)
    except Exception as e:
        raise ValueError(f"Ошибка чтения CSV: {e}")
    
    if not rows:
        raise ValueError("Пустой CSV файл")
    
    # Создаем новую книгу Excel
    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"
    
    # Записываем данные
    for row in rows:
        ws.append(row)
    
    # Настраиваем автоширину колонок (не менее 8 символов)
    for column in ws.columns:
        max_length = 0
        column_letter = column[0].column_letter
        for cell in column:
            try:
                if len(str(cell.value)) > max_length:
                    max_length = len(str(cell.value))
            except:
                pass
        adjusted_width = max(max_length + 2, 8)  # Минимум 8 символов
        ws.column_dimensions[column_letter].width = adjusted_width
    
    # Сохраняем файл
    xlsx_file = Path(xlsx_path)
    xlsx_file.parent.mkdir(parents=True, exist_ok=True)
    wb.save(xlsx_file)
```
![скриншот задания 1](/src/5%20лаба/img/1.1.png)

## Задание 2
```python
import json
import csv
from pathlib import Path


def json_to_csv(json_path: str, csv_path: str) -> None:
    """
    Преобразует JSON-файл в CSV.
    Поддерживает список словарей [{...}, {...}], заполняет отсутствующие поля пустыми строками.
    Кодировка UTF-8. Порядок колонок — алфавитный.
    """
    json_file = Path(json_path)
    if not json_file.exists():
        raise FileNotFoundError(f"JSON файл не найден: {json_path}")
    
    if not json_file.suffix.lower() == '.json':
        raise ValueError(f"Неверный тип файла: ожидается .json, получен {json_file.suffix}")
    
    try:
        with json_file.open('r', encoding='utf-8') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        raise ValueError(f"Ошибка парсинга JSON: {e}")
    
    if not data:
        raise ValueError("Пустой JSON или неподдерживаемая структура")
    
    if not isinstance(data, list):
        raise ValueError("JSON должен содержать список объектов")
    
    if not all(isinstance(item, dict) for item in data):
        raise ValueError("Все элементы JSON должны быть словарями")
    
    if not data:
        raise ValueError("Пустой список в JSON")
    
    # Собираем все возможные поля из всех объектов (алфавитный порядок)
    all_fields = set()
    for item in data:
        all_fields.update(item.keys())
    fieldnames = sorted(all_fields)
    
    csv_file = Path(csv_path)
    csv_file.parent.mkdir(parents=True, exist_ok=True)
    
    with csv_file.open('w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            # Заполняем отсутствующие поля пустыми строками
            complete_row = {field: row.get(field, '') for field in fieldnames}
            writer.writerow(complete_row)


def csv_to_json(csv_path: str, json_path: str) -> None:
    """
    Преобразует CSV в JSON (список словарей).
    Заголовок обязателен, значения сохраняются как строки.
    """
    csv_file = Path(csv_path)
    if not csv_file.exists():
        raise FileNotFoundError(f"CSV файл не найден: {csv_path}")
    
    if not csv_file.suffix.lower() == '.csv':
        raise ValueError(f"Неверный тип файла: ожидается .csv, получен {csv_file.suffix}")
    
    try:
        with csv_file.open('r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            rows = list(reader)
    except Exception as e:
        raise ValueError(f"Ошибка чтения CSV: {e}")
    
    if not rows:
        raise ValueError("Пустой CSV файл")
    
    json_file = Path(json_path)
    json_file.parent.mkdir(parents=True, exist_ok=True)
    
    with json_file.open('w', encoding='utf-8') as f:
        json.dump(rows, f, ensure_ascii=False, indent=2)
```
![скриншот задания 2](/src/5%20лаба/img/1.2.png)


# Лабораторная работа 6
## Задание 1.1
```python
#!/usr/bin/env python3
"""
CLI-утилиты для конвертации данных
"""

import argparse
import sys
import os

# Добавляем путь к корню проекта для импорта модулей
sys.path.insert(0, os.path.join(os.path.dirname(file), '../../..'))

try:
    from src.lab05.json_csv import json_to_csv, csv_to_json
    from src.lab05.csv_xlsx import csv_to_xlsx
except ImportError as e:
    print(f"Ошибка импорта модулей lab05: {e}")
    print("Убедитесь, что модули lab05 существуют и корректно реализованы")
    sys.exit(1)

def json2csv_command(input_file, output_file):
    """Конвертация JSON в CSV"""
    try:
        json_to_csv(input_file, output_file)
        print(f"Успешно сконвертировано: {input_file} -> {output_file}")
    except Exception as e:
        print(f"Ошибка при конвертации JSON в CSV: {e}")
        sys.exit(1)

def csv2json_command(input_file, output_file):
    """Конвертация CSV в JSON"""
    try:
        csv_to_json(input_file, output_file)
        print(f"Успешно сконвертировано: {input_file} -> {output_file}")
    except Exception as e:
        print(f"Ошибка при конвертации CSV в JSON: {e}")
        sys.exit(1)

def csv2xlsx_command(input_file, output_file):
    """Конвертация CSV в XLSX"""
    try:
        csv_to_xlsx(input_file, output_file)
        print(f"Успешно сконвертировано: {input_file} -> {output_file}")
    except Exception as e:
        print(f"Ошибка при конвертации CSV в XLSX: {e}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(
        description="Конвертеры данных между форматами JSON, CSV и XLSX",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    subparsers = parser.add_subparsers(dest="command", help="Доступные команды конвертации")

    # Подкоманда json2csv
    json2csv_parser = subparsers.add_parser("json2csv", help="Конвертировать JSON в CSV")
    json2csv_parser.add_argument("--in", dest="input", required=True, help="Входной JSON файл")
    json2csv_parser.add_argument("--out", dest="output", required=True, help="Выходной CSV файл")

    # Подкоманда csv2json
    csv2json_parser = subparsers.add_parser("csv2json", help="Конвертировать CSV в JSON")
    csv2json_parser.add_argument("--in", dest="input", required=True, help="Входной CSV файл")
    csv2json_parser.add_argument("--out", dest="output", required=True, help="Выходной JSON файл")

    # Подкоманда csv2xlsx
    csv2xlsx_parser = subparsers.add_parser("csv2xlsx", help="Конвертировать CSV в XLSX")
    csv2xlsx_parser.add_argument("--in", dest="input", required=True, help="Входной CSV файл")
    csv2xlsx_parser.add_argument("--out", dest="output", required=True, help="Выходной XLSX файл")

    args = parser.parse_args()

    if args.command == "json2csv":
        json2csv_command(args.input, args.output)
    elif args.command == "csv2json":
        csv2json_command(args.input, args.output)
    elif args.command == "csv2xlsx":
        csv2xlsx_command(args.input, args.output)
    else:
        parser.print_help()

if name == "main":
    main()
```
![скриншот задания 1](/src/5%20лаба/img/1.2.png)
## Задание 1.2
```python
#!/usr/bin/env python3
"""
CLI-утилиты для работы с текстом
"""

import argparse
import sys
import re
from collections import Counter

def read_file(file_path):
    """
    Чтение файла с автоматическим определением кодировки
    """
    encodings = ['utf-8', 'cp1251', 'iso-8859-1', 'windows-1251']
    
    for encoding in encodings:
        try:
            with open(file_path, 'r', encoding=encoding) as file:
                return file.read()
        except UnicodeDecodeError:
            continue
            
    raise UnicodeDecodeError(f"Не удалось декодировать файл {file_path}")

def calculate_word_frequency(text):
    """
    Анализ частотности слов в тексте
    """
    # Приводим к нижнему регистру и находим слова
    words = re.findall(r'\b[а-яёa-z]+\b', text.lower())
    return Counter(words)

def get_top_words(frequency, top_n=5):
    """
    Получение топ-N самых частых слов
    """
    return frequency.most_common(top_n)

def cat_command(input_file, number_lines=False):
    """
    Реализация команды cat - вывод содержимого файла
    """
    try:
        content = read_file(input_file)
        lines = content.split('\n')
        
        for i, line in enumerate(lines, 1):
            if number_lines:
                print(f"{i:6d}\t{line}")
            else:
                print(line)
                
    except FileNotFoundError:
        print(f"Ошибка: файл '{input_file}' не найден")
        sys.exit(1)
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        sys.exit(1)

def stats_command(input_file, top_n=5):
    """
    Реализация команды stats - анализ частот слов
    """
    try:
        content = read_file(input_file)
        if not content.strip():
            print("Файл пуст")
            return
            
        frequency = calculate_word_frequency(content)
        top_words = get_top_words(frequency, top_n)
        
        print(f"Топ-{top_n} самых частых слов в файле '{input_file}':")
        print("-" * 40)
        for i, (word, count) in enumerate(top_words, 1):
            print(f"{i:2d}. {word:<15} {count:>4} раз")
            
    except FileNotFoundError:
        print(f"Ошибка: файл '{input_file}' не найден")
        sys.exit(1)
    except Exception as e:
        print(f"Ошибка при анализе текста: {e}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(
        description="CLI-утилиты для работы с текстом",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    subparsers = parser.add_subparsers(dest="command", help="Доступные команды")

    # Подкоманда cat
    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True, help="Входной файл")
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    # Подкоманда stats
    stats_parser = subparsers.add_parser("stats", help="Анализ частот слов")
    stats_parser.add_argument("--input", required=True, help="Входной текстовый файл")
    stats_parser.add_argument("--top", type=int, default=5, help="Количество топ-слов (по умолчанию: 5)")

    args = parser.parse_args()

    if args.command == "cat":
        cat_command(args.input, args.n)
    elif args.command == "stats":
        stats_command(args.input, args.top)
    else:
        parser.print_help()

if name == "main":
    main()
```
![скриншот задания 2](/src/5%20лаба/img/1.2.png)








