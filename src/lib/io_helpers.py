"""
Вспомогательные функции для ввода/вывода
"""

import json
import csv

def read_file(file_path):
    """Чтение файла с автоматическим определением кодировки"""
    encodings = ['utf-8', 'cp1251', 'iso-8859-1']
    
    for encoding in encodings:
        try:
            with open(file_path, 'r', encoding=encoding) as file:
                return file.read()
        except UnicodeDecodeError:
            continue
            
    raise UnicodeDecodeError(f"Не удалось декодировать файл {file_path} с помощью кодировок: {encodings}")

def write_file(file_path, content):
    """Запись в файл в кодировке UTF-8"""
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def read_json(file_path):
    """Чтение JSON файла"""
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def write_json(file_path, data):
    """Запись данных в JSON файл"""
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)

def read_csv(file_path):
    """Чтение CSV файла"""
    with open(file_path, 'r', encoding='utf-8') as file:
        return list(csv.reader(file))

def write_csv(file_path, data):
    """Запись данных в CSV файл"""
    with open(file_path, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)