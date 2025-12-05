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