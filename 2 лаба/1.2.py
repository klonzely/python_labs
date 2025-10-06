m=[[1, 2, 3]]
def transpose(mat: list[list[float | int]]) -> list[list]:
    if not m:
        raise ValueError("Список пустой")
    else:
        q=[]
        q.append(zip(m))
        return q
print(transpose(m))