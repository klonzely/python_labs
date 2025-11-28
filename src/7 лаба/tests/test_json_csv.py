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