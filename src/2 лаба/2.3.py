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