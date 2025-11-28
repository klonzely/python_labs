tests/test_text.py
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