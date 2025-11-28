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

if __name__ == "main":
    main()