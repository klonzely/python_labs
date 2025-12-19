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
# Лабораторная работа 7
## Задание 1.1
```python
import pytest
from src.lib.text import normalize, tokenize, count_freq, top_n


class TestNormalize:
    """Тесты для функции normalize"""

    @pytest.mark.parametrize(
        "source, expected",
        [
            ("ПрИвЕт\nМИр\t", "привет мир"),
            ("ёжик, Ёлка", "ежик, елка"),
            ("Hello\r\nWorld", "hello world"),
            ("  двойные   пробелы  ", "двойные пробелы"),
            ("", ""),
            ("   ", ""),
            ("ТЕСТ", "тест"),
            ("много\t\t\tтабов", "много табов"),
        ],
    )
    def test_normalize_basic(self, source, expected):
        assert normalize(source) == expected


class TestTokenize:
    """Тесты для функции tokenize"""

    @pytest.mark.parametrize(
        "source, expected",
        [
            ("привет мир", ["привет", "мир"]),
            ("hello world test", ["hello", "world", "test"]),
            ("", []),
            ("   ", []),
            ("только, пунктуация!?", []),
            ("смешанный text с English", ["смешанный", "text", "с", "english"]),
            ("много     пробелов", ["много", "пробелов"]),
        ],
    )
    def test_tokenize_basic(self, source, expected):
        assert tokenize(source) == expected


class TestCountFreq:
    """Тесты для функции count_freq"""

    def test_count_freq_basic(self):
        tokens = ["apple", "banana", "apple", "cherry", "banana", "apple"]
        expected = {"apple": 3, "banana": 2, "cherry": 1}
        assert count_freq(tokens) == expected

    def test_count_freq_empty(self):
        assert count_freq([]) == {}

    def test_count_freq_single(self):
        assert count_freq(["test"]) == {"test": 1}

    def test_count_freq_duplicates(self):
        tokens = ["word", "word", "word"]
        assert count_freq(tokens) == {"word": 3}


class TestTopN:
    """Тесты для функции top_n"""

    def test_top_n_basic(self):
        freq = {"apple": 5, "banana": 3, "cherry": 7, "date": 1}
        result = top_n(freq, 3)
        expected = [("cherry", 7), ("apple", 5), ("banana", 3)]
        assert result == expected

    def test_top_n_tie_breaker(self):
        # Проверка сортировки по алфавиту при равных частотах
        freq = {"zebra": 3, "apple": 3, "banana": 3, "cherry": 2}
        result = top_n(freq, 4)
        expected = [("apple", 3), ("banana", 3), ("zebra", 3), ("cherry", 2)]
        assert result == expected

    def test_top_n_empty(self):
        assert top_n({}, 5) == []

    def test_top_n_zero_n(self):
        assert top_n({"a": 1}, 0) == []

    def test_top_n_more_than_available(self):
        freq = {"a": 1, "b": 2}
        result = top_n(freq, 5)
        assert len(result) == 2
        assert result == [("b", 2), ("a", 1)]

    def test_top_n_single(self):
        assert top_n({"test": 5}, 1) == [("test", 5)]
```
![скриншот задания 1](/src/5%20лаба/img/1.2.png)
## Задание 2
```python
import pytest
import json
import csv
from pathlib import Path
from src.lab05.json_csv import json_to_csv, csv_to_json


class TestJsonToCsv:
    """Тесты для функции json_to_csv"""

    def test_json_to_csv_basic(self, tmp_path: Path):
        """Позитивный тест конвертации JSON в CSV"""
        src = tmp_path / "test.json"
        dst = tmp_path / "test.csv"

        data = [
            {"name": "Alice", "age": 22, "city": "Moscow"},
            {"name": "Bob", "age": 25, "city": "SPb"},
            {"name": "Charlie", "age": 30},
        ]

        src.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        json_to_csv(str(src), str(dst))

        # Проверяем что файл создан
        assert dst.exists()

        # Проверяем содержимое CSV
        with open(dst, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            rows = list(reader)

        assert len(rows) == 3
        assert set(rows[0].keys()) == {"age", "city", "name"}
        assert rows[0]["name"] == "Alice"
        assert rows[0]["age"] == "22"
        assert rows[0]["city"] == "Moscow"

    def test_json_to_csv_roundtrip(self, tmp_path: Path):
        """Тест полного цикла JSON -> CSV -> JSON"""
        src_json = tmp_path / "src.json"
        intermediate_csv = tmp_path / "intermediate.csv"
        dst_json = tmp_path / "dst.json"

        original_data = [{"id": 1, "value": "test1"}, {"id": 2, "value": "test2"}]

        # Сохраняем исходный JSON
        src_json.write_text(json.dumps(original_data), encoding="utf-8")

        # Конвертируем в CSV
        json_to_csv(str(src_json), str(intermediate_csv))

        # Конвертируем обратно в JSON
        csv_to_json(str(intermediate_csv), str(dst_json))

        # Читаем результат
        with open(dst_json, "r", encoding="utf-8") as f:
            result_data = json.load(f)

        # Проверяем что данные сохранились
        assert len(result_data) == len(original_data)
        assert result_data[0]["id"] == "1"  # CSV конвертирует числа в строки
        assert result_data[0]["value"] == "test1"

    def test_json_to_csv_file_not_found(self):
        """Тест на несуществующий файл"""
        with pytest.raises(FileNotFoundError):
            json_to_csv("nonexistent.json", "output.csv")

    def test_json_to_csv_invalid_json(self, tmp_path: Path):
        """Тест на некорректный JSON"""
        src = tmp_path / "invalid.json"
        dst = tmp_path / "output.csv"

        src.write_text("{invalid json}", encoding="utf-8")

        with pytest.raises(ValueError):
            json_to_csv(str(src), str(dst))

    def test_json_to_csv_empty_json(self, tmp_path: Path):
        """Тест на пустой JSON"""
        src = tmp_path / "empty.json"
        dst = tmp_path / "output.csv"

        src.write_text("[]", encoding="utf-8")

        with pytest.raises(ValueError):
            json_to_csv(str(src), str(dst))

    def test_json_to_csv_not_array(self, tmp_path: Path):
        """Тест на JSON не являющийся массивом объектов"""
        src = tmp_path / "not_array.json"
        dst = tmp_path / "output.csv"

        src.write_text('{"key": "value"}', encoding="utf-8")

        with pytest.raises(ValueError):
            json_to_csv(str(src), str(dst))


class TestCsvToJson:
    """Тесты для функции csv_to_json"""

    def test_csv_to_json_basic(self, tmp_path: Path):
        """Позитивный тест конвертации CSV в JSON"""
        src = tmp_path / "test.csv"
        dst = tmp_path / "test.json"

        # Создаем CSV файл
        with open(src, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["name", "age", "city"])
            writer.writeheader()
            writer.writerow({"name": "Alice", "age": "22", "city": "Moscow"})
            writer.writerow({"name": "Bob", "age": "25", "city": "SPb"})

        csv_to_json(str(src), str(dst))

        # Проверяем что файл создан
        assert dst.exists()


# Проверяем содержимое JSON
        with open(dst, "r", encoding="utf-8") as f:
            data = json.load(f)

        assert len(data) == 2
        assert data[0]["name"] == "Alice"
        assert data[0]["age"] == "22"
        assert data[0]["city"] == "Moscow"

    def test_csv_to_json_file_not_found(self):
        """Тест на несуществующий файл"""
        with pytest.raises(FileNotFoundError):
            csv_to_json("nonexistent.csv", "output.json")

    def test_csv_to_json_invalid_csv(self, tmp_path: Path):
        """Тест на некорректный CSV"""
        src = tmp_path / "invalid.csv"
        dst = tmp_path / "output.json"

        src.write_text(
            "invalid,csv,content\nline1,without,enough,columns", encoding="utf-8"
        )

        with pytest.raises(ValueError):
            csv_to_json(str(src), str(dst))

    def test_csv_to_json_empty_csv(self, tmp_path: Path):
        """Тест на пустой CSV"""
        src = tmp_path / "empty.csv"
        dst = tmp_path / "output.json"

        src.write_text("", encoding="utf-8")

        with pytest.raises(ValueError):
            csv_to_json(str(src), str(dst))
```
![скриншот задания 2](/src/5%20лаба/img/1.2.png)
## Задание 3
```python
[build-system]
requires = ["setuptools>=45.0", "wheel"]
build-backend = "setuptools.build_meta"

[tool.black]
line-length = 88
target-version = ['py38', 'py39', 'py310']
include = '\.pyi?$'
extend-exclude = '''
/(
  | \.eggs
  | \.git
  | \.hg
  | \.mypy_cache
  | \.tox
  | \.venv
  | build
  | dist
)/
'''

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
python_classes = ["Test*"]
python_functions = ["test_*"]
addopts = [
    "--verbose",
    "--strict-markers",
    "--strict-config",
    "--cov=src",
    "--cov-report=term-missing"
]

[tool.coverage.run]
source = ["src"]
omit = ["*/tests/*", "*/test_*"]
```
![скриншот задания 3](/src/5%20лаба/img/1.2.png)
# Лабораторная работа 8
## Задание 1
```python
from dataclasses import dataclass, field
from datetime import datetime, date
from typing import Dict, Any


@dataclass
class Student:
    """Модель студента с валидацией данных."""
    
    fio: str
    birthdate: str  # Формат: YYYY-MM-DD
    group: str
    gpa: float
    _birthdate_obj: date = field(init=False, repr=False)  # Внутренний объект даты
    
    def __post_init__(self):
        """Валидация данных после инициализации объекта."""
        # Валидация даты
        try:
            self._birthdate_obj = datetime.strptime(self.birthdate, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("Дата должна быть в формате YYYY-MM-DD")
        
        # Валидация среднего балла
        if not 0 <= self.gpa <= 5:
            raise ValueError("Средний балл должен быть в диапазоне от 0 до 5")
    
    def age(self) -> int:
        """Вычисляет возраст студента на текущую дату."""
        today = date.today()
        age = today.year - self._birthdate_obj.year
        
        # Корректировка, если день рождения в этом году еще не наступил
        if (today.month, today.day) < (self._birthdate_obj.month, self._birthdate_obj.day):
            age -= 1
        
        return age
    
    def to_dict(self) -> Dict[str, Any]:
        """Преобразует объект студента в словарь."""
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Student':
        """Создает объект студента из словаря."""
        return cls(
            fio=data["fio"],
            birthdate=data["birthdate"],
            group=data["group"],
            gpa=data["gpa"]
        )
    
    def __str__(self) -> str:
        """Строковое представление студента."""
        return (f"Студент: {self.fio}\n"
                f"Дата рождения: {self.birthdate} (Возраст: {self.age()})\n"
                f"Группа: {self.group}\n"
                f"Средний балл: {self.gpa:.2f}")


# Пример использования
if __name__ == "__main__":
    try:
        # Создание студента
        student = Student(
            fio="Иванов Иван Иванович",
            birthdate="2000-05-15",
            group="ИТ-101",
            gpa=4.5
        )
        
        # Тестирование методов
        print(student)
        print("\nСловарь:", student.to_dict())
        
        # Создание из словаря
        student2 = Student.from_dict({
            "fio": "Петров Петр Петрович",
            "birthdate": "2001-08-20",
            "group": "ФИ-201",
            "gpa": 3.8
        })
        print(f"\n{student2}")
        
        # Тест валидации (раскомментировать для проверки)
        # student3 = Student("Тест", "2000-13-45", "Группа", 6.0)  # Ошибка валидации
        
    except ValueError as e:
        print(f"Ошибка валидации: {e}")
```
![скриншот задания 1](/src/8%20лаба/img/№1.png)
## Задание 2
```python
import json
from pathlib import Path
from typing import List, Optional
from .models import Student

def students_to_json(students: List[Student], path: str) -> None:
    """
    Сохраняет список студентов в JSON файл.
    
    Args:
        students (List[Student]): Список объектов Student
        path (str): Путь к файлу для сохранения
        
    Raises:
        ValueError: Если передан не список или путь некорректен
    """
    if not isinstance(students, list):
        raise ValueError("Ожидается список объектов Student")
    
    if not all(isinstance(s, Student) for s in students):
        raise ValueError("Все элементы списка должны быть объектами Student")
    
    # Преобразуем студентов в словари
    data = [student.to_dict() for student in students]
    
    # Создаем директорию, если она не существует
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    
    # Сохраняем в JSON
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"Данные успешно сохранены в {path}")

def students_from_json(path: str) -> List[Student]:
    """
    Загружает список студентов из JSON файла.
    
    Args:
        path (str): Путь к JSON файлу
        
    Returns:
        List[Student]: Список объектов Student
        
    Raises:
        FileNotFoundError: Если файл не найден
        ValueError: Если данные в файле некорректны
    """
    if not Path(path).exists():
        raise FileNotFoundError(f"Файл {path} не найден")
    
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        raise ValueError(f"Ошибка чтения JSON: {e}")
    
    if not isinstance(data, list):
        raise ValueError("Данные должны быть списком")
    
    students = []
    errors = []
    
    for i, item in enumerate(data):
        try:
            # Проверяем обязательные поля
            required_fields = ["fio", "birthdate", "group", "gpa"]
            for field in required_fields:
                if field not in item:
                    raise ValueError(f"Отсутствует обязательное поле: {field}")
            
            # Создаем студента
            student = Student.from_dict(item)
            students.append(student)
            
        except (ValueError, TypeError) as e:
            errors.append(f"Запись {i}: {e}")
    
    if errors:
        print("Обнаружены ошибки при загрузке:")
        for error in errors:
            print(f"  - {error}")
    
    print(f"Загружено {len(students)} студентов из {path}")
    return students
```
![скриншот задания 2](/src/8%20лаба/img/№1.png)
# Лабораторная работа 9
## Задание 1
```python
"""
Класс Group - реализация CRUD-операций над студентами в CSV-файле
"""

import csv
from pathlib import Path
from typing import List, Optional, Dict, Any
import statistics

# Абсолютный импорт
import sys
import os

# Добавляем путь к src в sys.path
sys.path.insert(0, os.path.join(os.path.dirname(file), '..'))

from lab08.models import Student


class Group:
    """Класс для управления коллекцией студентов в CSV-файле."""
    
    CSV_HEADER = ["fio", "birthdate", "group", "gpa"]
    
    def init(self, storage_path: str):
        """
        Инициализация группы студентов.
        
        Args:
            storage_path (str): Путь к CSV-файлу для хранения данных
        """
        self.path = Path(storage_path)
        self._ensure_storage_exists()
    
    
    def _ensure_storage_exists(self) -> None:
        """
        Создает файл с заголовком, если он не существует.
        """
        if not self.path.exists():
            # Создаем директорию, если её нет
            self.path.parent.mkdir(parents=True, exist_ok=True)
            
            # Создаем файл с заголовком
            with open(self.path, 'w', encoding='utf-8', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=self.CSV_HEADER)
                writer.writeheader()
            print(f"Создан новый файл: {self.path}")
    
    def _read_all_rows(self) -> List[Dict[str, str]]:
        """
        Читает все строки из CSV-файла.
        
        Returns:
            List[Dict[str, str]]: Список словарей с данными студентов
        
        Raises:
            ValueError: Если файл поврежден или имеет неверный формат
        """
        rows = []
        
        try:
            with open(self.path, 'r', encoding='utf-8', newline='') as f:
                reader = csv.DictReader(f)
                
                # Проверяем наличие заголовка
                if reader.fieldnames != self.CSV_HEADER:
                    raise ValueError(
                        f"Неверный формат CSV. Ожидаемые поля: {self.CSV_HEADER}, "
                        f"полученные: {reader.fieldnames}"
                    )
                
                for row_num, row in enumerate(reader, start=2):  # Начинаем с 2 (1 - заголовок)
                    try:
                        # Проверяем обязательные поля
                        for field in self.CSV_HEADER:
                            if field not in row:
                                raise ValueError(f"Отсутствует поле '{field}' в строке {row_num}")
                        
                        # Валидируем данные через создание объекта Student
                        Student(
                            fio=row['fio'],
                            birthdate=row['birthdate'],
                            group=row['group'],
                            gpa=float(row['gpa'])
                        )
                        
                        rows.append(row)
                        
                    except (ValueError, TypeError) as e:
                        print(f"Предупреждение: Пропущена строка {row_num}: {e}")
                        continue
                        
        except FileNotFoundError:
            print(f"Файл не найден: {self.path}")
            return []
        except Exception as e:
            raise ValueError(f"Ошибка чтения файла {self.path}: {e}")
        
        return rows
    
    def list(self) -> List[Student]:
        """
        Возвращает список всех студентов.
        
        Returns:
            List[Student]: Список объектов Student
        """
        rows = self._read_all_rows()
        students = []
        
        for row in rows:
            try:
                student = Student(
                    fio=row['fio'],
                    birthdate=row['birthdate'],
                    group=row['group'],
                    gpa=float(row['gpa'])
                )
                students.append(student)
            except (ValueError, TypeError) as e:
                print(f"Предупреждение: Не удалось создать студента из строки: {e}")
                continue
        
        return students
    
    def add(self, student: Student) -> None:
        """
        Добавляет нового студента в CSV-файл.
        
        Args:
            student (Student): Объект студента для добавления
        
        Raises:
            ValueError: Если студент с таким ФИО уже существует
        """
        # Проверяем, нет ли уже студента с таким ФИО
        existing_students = self.list()
        for existing in existing_students:
            if existing.fio == student.fio:
                raise ValueError(f"Студент с ФИО '{student.fio}' уже существует")
        
        # Добавляем новую запись
        with open(self.path, 'a', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=self.CSV_HEADER)
            writer.writerow({
                'fio': student.fio,
                'birthdate': student.birthdate,
                'group': student.group,
                'gpa': student.gpa
            })
        
        print(f"Добавлен студент: {student.fio}")
    
    def find(self, substr: str) -> List[Student]:
        """
        Ищет студентов по подстроке в ФИО.
        
        Args:
            substr (str): Подстрока для поиска в ФИО
        
        Returns:
            List[Student]: Список найденных студентов
        """
        if not substr:
            return []
        
        all_students = self.list()
        found_students = []
        
        for student in all_students:
            if substr.lower() in student.fio.lower():
                found_students.append(student)
        
        return found_students
    
    def remove(self, fio: str) -> bool:
        """
        Удаляет студента по ФИО.
        
        Args:
            fio (str): ФИО студента для удаления
        
        Returns:
            bool: True если студент был удален, False если не найден
        """
        rows = self._read_all_rows()
        initial_count = len(rows)
        
        # Фильтруем строки, оставляя только те, где ФИО не совпадает
        filtered_rows = [row for row in rows if row['fio'] != fio]
        
        if len(filtered_rows) == initial_count:
            print(f"Студент с ФИО '{fio}' не найден")
            return False
        
        # Записываем обновленные данные
        with open(self.path, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=self.CSV_HEADER)
            writer.writeheader()
            writer.writerows(filtered_rows)
        
        print(f"Удален студент: {fio}")
        return True
    
    def update(self, fio: str, **fields) -> bool:
        """
        Обновляет поля существующего студента.
        
        Args:
            fio (str): ФИО студента для обновления
            **fields: Поля для обновления (fio, birthdate, group, gpa)
        
        Returns:
            bool: True если студент был обновлен, False если не найден
        
        Raises:
            ValueError: Если переданы некорректные поля
        """
        # Проверяем допустимость полей
        valid_fields = set(self.CSV_HEADER)
        invalid_fields = set(fields.keys()) - valid_fields
        if invalid_fields:
            raise ValueError(f"Недопустимые поля: {invalid_fields}. Допустимые: {valid_fields}")
        
        rows = self._read_all_rows()
        updated = False
        
        for row in rows:
            if row['fio'] == fio:
                # Обновляем поля
                for key, value in fields.items():
                    row[key] = value
                
                # Валидируем обновленные данные
                try:
                    Student(
                        fio=row['fio'],
                        birthdate=row['birthdate'],
                        group=row['group'],
                        gpa=float(row['gpa'])
                    )
                except (ValueError, TypeError) as e:
                    raise ValueError(f"Некорректные данные для обновления: {e}")
                
                updated = True
                break
            if not updated:
                print(f"Студент с ФИО '{fio}' не найден")
            return False
        
        # Записываем обновленные данные
        with open(self.path, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=self.CSV_HEADER)
            writer.writeheader()
            writer.writerows(rows)
        
        print(f"Обновлен студент: {fio}")
        return True
    
    def stats(self) -> Dict[str, Any]:
        """
        Возвращает статистику по студентам.
        
        Returns:
            Dict[str, Any]: Словарь со статистикой
        
        Raises:
            ValueError: Если нет студентов для анализа
        """
        students = self.list()
        
        if not students:
            raise ValueError("Нет студентов для анализа")
        
        # Собираем GPA для вычислений
        gpa_list = [student.gpa for student in students]
        
        # Группируем по группам
        groups_count = {}
        for student in students:
            group = student.group
            groups_count[group] = groups_count.get(group, 0) + 1
        
        # Топ-5 студентов по GPA
        sorted_students = sorted(students, key=lambda s: s.gpa, reverse=True)
        top_5 = [
            {"fio": s.fio, "gpa": s.gpa, "group": s.group}
            for s in sorted_students[:5]
        ]
        
        return {
            "count": len(students),
            "min_gpa": min(gpa_list),
            "max_gpa": max(gpa_list),
            "avg_gpa": statistics.mean(gpa_list) if gpa_list else 0,
            "median_gpa": statistics.median(gpa_list) if gpa_list else 0,
            "groups": groups_count,
            "top_5_students": top_5,
            "age_distribution": {
                "youngest": min(students, key=lambda s: s.age()).age(),
                "oldest": max(students, key=lambda s: s.age()).age(),
                "avg_age": statistics.mean([s.age() for s in students])
            }
        }
    
    def clear(self) -> None:
        """
        Очищает все записи студентов, оставляя только заголовок.
        """
        with open(self.path, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=self.CSV_HEADER)
            writer.writeheader()
        
        print(f"База данных очищена: {self.path}")
    
    def import_from_json(self, json_path: str) -> int:
        """
        Импортирует студентов из JSON файла.
        
        Args:
            json_path (str): Путь к JSON файлу
        
        Returns:
            int: Количество импортированных студентов
        """
        from ..lab08.serialize import students_from_json
        
        imported_students = students_from_json(json_path)
        imported_count = 0
        
        for student in imported_students:
            try:
                self.add(student)
                imported_count += 1
            except ValueError as e:
                print(f"Не удалось импортировать {student.fio}: {e}")
        
        print(f"Импортировано {imported_count} студентов из {json_path}")
        return imported_count
    
    def export_to_json(self, json_path: str) -> None:
        """
        Экспортирует студентов в JSON файл.
        
        Args:
            json_path (str): Путь для сохранения JSON файла
        """
        from ..lab08.serialize import students_to_json
        
        students = self.list()
        students_to_json(students, json_path)
        print(f"Экспортировано {len(students)} студентов в {json_path}")
    
    def len(self) -> int:
        """
        Возвращает количество студентов в группе.
        
        Returns:
            int: Количество студентов
        """
        return len(self.list())
    
    def str(self) -> str:
        """
        Строковое представление группы.
        
        Returns:
            str: Информация о группе
        """
        students = self.list()
        return f"Группа (файл: {self.path}): {len(students)} студентов"
```
# Лабораторная работа 10
## Задание 1
```python
from collections import deque
from typing import Any


class Stack:
    """Структура данных стек (LIFO) на базе list."""
    
    def __init__(self) -> None:
        """Инициализирует пустой стек."""
        self._data: list[Any] = []
    
    def push(self, item: Any) -> None:
        """Добавляет элемент на вершину стека.
        
        Args:
            item: Элемент для добавления в стек.
        """
        self._data.append(item)
    
    def pop(self) -> Any:
        """Удаляет и возвращает верхний элемент стека.
        
        Returns:
            Верхний элемент стека.
            
        Raises:
            IndexError: Если стек пуст.
        """
        if self.is_empty():
            raise IndexError("Попытка извлечения из пустого стека")
        return self._data.pop()
    
    def peek(self) -> Any | None:
        """Возвращает верхний элемент стека без удаления.
        
        Returns:
            Верхний элемент стека или None, если стек пуст.
        """
        return self._data[-1] if not self.is_empty() else None
    
    def is_empty(self) -> bool:
        """Проверяет, пуст ли стек.
        
        Returns:
            True, если стек пуст, иначе False.
        """
        return len(self._data) == 0
    
    def __len__(self) -> int:
        """Возвращает количество элементов в стеке.
        
        Returns:
            Количество элементов в стеке.
        """
        return len(self._data)
    
    def __str__(self) -> str:
        """Строковое представление стека.
        
        Returns:
            Строковое представление стека.
        """
        return f"Stack({self._data})"
    
    def __repr__(self) -> str:
        """Официальное строковое представление стека.
        
        Returns:
            Официальное строковое представление стека.
        """
        return f"Stack({self._data})"


class Queue:
    """Структура данных очередь (FIFO) на базе deque."""
    
    def __init__(self) -> None:
        """Инициализирует пустую очередь."""
        self._data: deque[Any] = deque()
    
    def enqueue(self, item: Any) -> None:
        """Добавляет элемент в конец очереди.
        
        Args:
            item: Элемент для добавления в очередь.
        """
        self._data.append(item)
    
    def dequeue(self) -> Any:
        """Удаляет и возвращает элемент из начала очереди.
        
        Returns:
            Элемент из начала очереди.
            
        Raises:
            IndexError: Если очередь пуста.
        """
        if self.is_empty():
            raise IndexError("Попытка извлечения из пустой очереди")
        return self._data.popleft()
    
    def peek(self) -> Any | None:
        """Возвращает элемент из начала очереди без удаления.
        
        Returns:
            Элемент из начала очереди или None, если очередь пуста.
        """
        return self._data[0] if not self.is_empty() else None
    
    def is_empty(self) -> bool:
        """Проверяет, пуста ли очередь.
        
        Returns:
            True, если очередь пуста, иначе False.
        """
        return len(self._data) == 0
    
    def __len__(self) -> int:
        """Возвращает количество элементов в очереди.
        
        Returns:
            Количество элементов в очереди.
        """
        return len(self._data)
    
    def __str__(self) -> str:
        """Строковое представление очереди.
        
        Returns:
            Строковое представление очереди.
        """
        return f"Queue({list(self._data)})"
    
    def __repr__(self) -> str:
        """Официальное строковое представление очереди.
        
        Returns:
            Официальное строковое представление очереди.
        """
        return f"Queue({list(self._data)})"
```
![скриншот задания 2](/src/8%20лаба/img/№1.png)
## Задание 2
```python
from typing import Any, Optional, Iterator


class Node:
    """Узел односвязного списка"""
    
    def __init__(self, value: Any, next_node: Optional['Node'] = None):
        self.value = value
        self.next = next_node
    
    def __repr__(self) -> str:
        return f"Node({self.value})"


class SinglyLinkedList:
    """Односвязный список"""
    
    def __init__(self):
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self._size: int = 0
    
    def append(self, value: Any) -> None:
        """Добавить элемент в конец списка за O(1)"""
        new_node = Node(value)
        
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        
        self._size += 1
    
    def prepend(self, value: Any) -> None:
        """Добавить элемент в начало списка за O(1)"""
        new_node = Node(value)
        
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        
        self._size += 1
    
    def insert(self, idx: int, value: Any) -> None:
        """Вставить элемент по индексу idx"""
        if idx < 0 or idx > self._size:
            raise IndexError(f"Index {idx} out of range [0, {self._size}]")
        
        if idx == 0:
            self.prepend(value)
        elif idx == self._size:
            self.append(value)
        else:
            current = self.head
            for _ in range(idx - 1):
                current = current.next
            
            new_node = Node(value, current.next)
            current.next = new_node
            self._size += 1
    
    def remove_at(self, idx: int) -> None:
        """Удалить элемент по индексу idx"""
        if idx < 0 or idx >= self._size:
            raise IndexError(f"Index {idx} out of range [0, {self._size})")
        
        if idx == 0:  # Удаление из начала
            self.head = self.head.next
            if self.head is None:  # Если список стал пустым
                self.tail = None
        else:
            current = self.head
            for _ in range(idx - 1):
                current = current.next
            
            # current теперь указывает на узел перед удаляемым
            current.next = current.next.next
            
            # Если удалили последний элемент
            if current.next is None:
                self.tail = current
        
        self._size -= 1
    
    def remove(self, value: Any) -> None:
        """Удалить первое вхождение значения value"""
        if self.is_empty():
            return
        
        # Если удаляем из начала
        if self.head.value == value:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self._size -= 1
            return
        
        # Ищем узел перед тем, который нужно удалить
        current = self.head
        while current.next and current.next.value != value:
            current = current.next
        
        # Если нашли значение
        if current.next and current.next.value == value:
            current.next = current.next.next
            self._size -= 1
            
            # Если удалили последний элемент
            if current.next is None:
                self.tail = current
    
    def is_empty(self) -> bool:
        """Проверка, пуст ли список"""
        return self.head is None
    
    def __iter__(self) -> Iterator[Any]:
        """Итератор по значениям списка"""
        current = self.head
        while current:
            yield current.value
            current = current.next
    
    def __len__(self) -> int:
        """Количество элементов в списке"""
        return self._size
    
    def __repr__(self) -> str:
        """Строковое представление списка"""
        values = list(self)
        return f"SinglyLinkedList({values})"
    
    def __getitem__(self, idx: int) -> Any:
        """Получить значение по индексу (дополнительный метод)"""
        if idx < 0 or idx >= self._size:
            raise IndexError(f"Index {idx} out of range [0, {self._size})")
        
        current = self.head
        for _ in range(idx):
            current = current.next
        return current.value
```







