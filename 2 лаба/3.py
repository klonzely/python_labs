# inp = ('иванов иван иванович', 'BIVT-25', 4.6)
# def format_record(rec: tuple[str, str, float]) -> str:
#     """Некорректные записи -> ValueError"""
#     fio, group, gpa = inp[0], inp[1], inp[2]
#     if fio == '' or group == '' or type(gpa) != float:
#         return 'ValueError'
#     fio = fio.split()
#     for i in range(len(fio)):
#         fio[i] = fio[i][0].upper() + fio[i][1:]
#     return f'{fio[0]} {fio[1][0]}.{fio[2][0]}., гр. {group}, GPA {gpa:.2f}'
# print(format_record(inp))
print('иванов иван иванович'.split())