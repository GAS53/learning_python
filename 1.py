
class Matrix():
    def __init__(self, in_li_lists):
        self.main_li = in_li_lists

    def __str__(self):
        res = ''
        for i in self.main_li:
            res += '\n'
            for j in i:
                res += f"{j} "
        return res


class Matrix2(Matrix):

    def __add__(self, new):
        new_matrix = []
        for num_i, i in enumerate(self.main_li):
            inner_li = []
            for num_j, j in enumerate(i):
                inner_li.append(j+new.main_li[num_i][num_j])
            new_matrix.append(inner_li)

        return Matrix(new_matrix)


li_lists = [[1, 2, 3, 4, 5], [2, 5, 76, 72]]
mx = Matrix(li_lists)
# print(mx)  # test __str__


mx1 = Matrix2([[1, 2, 3, 4, 5], [2, 5, 76, 72]])
mx2 = Matrix2([[1, 1, 1, 1, 1], [1, 1, 1, 1]])
mx3 = mx1 + mx2
print(mx3)  # test __add__
