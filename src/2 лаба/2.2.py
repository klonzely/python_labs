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