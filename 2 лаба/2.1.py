mat=[[1, 2, 3]]
def transpose(mat: list[list[float | int]]) -> list[list]:
    if len(mat)==0:
        return []
    for i in range (len(mat)):
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
