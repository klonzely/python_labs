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