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




# Лабораторная работа 3
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







