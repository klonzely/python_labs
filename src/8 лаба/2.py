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