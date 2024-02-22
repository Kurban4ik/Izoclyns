def multiply(a, b):
    if len(a[0]) == len(b):
        out = []
        for i in range(len(a)):
            out.append([0] * len(b[0]))
        for i in range(len(a)):
            for j in range(len(b[0])):
                for k in range(len(a[0])):
                    out[i][j] += a[i][k] * b[k][j]
        return out
    else:
        raise 'Дебил'


def sum_mat(a, b):
    return [a[i][j] + b[i][j] for i in range(len(a)) for j in range(len(a[0]))]


class Affiner:
    def __init__(self, mat, size, diff_mat):
        self.mat = mat
        self.size = size
        self.diff = diff_mat

    def change_vector_or_point(self, vec):
        return sum_mat(multiply(self.mat, vec), self.diff)


t = Affiner([[1, 2], [3, 4]], 2, [[0], [0]])
print(t.change_vector_or_point([[1], [1]]))
