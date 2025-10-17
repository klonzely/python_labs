normalize_test_case = [
 "ПрИвЕт\nМИр\t",      # "привет мир"
  "ёжик, Ёлка",        # "ежик, елка"
  "Hello\r\nWorld",    # "hello world"
  "  двойные   пробелы  "    # "двойные пробелы"
]


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

for i in normalize_test_case:
    print(f'"{i}" -> "{normalize(i)}"')