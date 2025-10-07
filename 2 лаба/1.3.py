mat = [[1, 2], [3, 4]]
def flatten(mat: list[list | tuple]) -> list:
    if all(type(x) == list or type(x) == tuple for x in mat):
        return [mat[i][j] for i in range(len(mat)) for j in range(len(mat[i]))]
    else:
        return 'TypeError'
print(flatten(mat))