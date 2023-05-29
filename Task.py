class Matrix:

    def __init__(self, matrix: list) -> None:
        self.matrix = matrix

    def transpose(self, other):
        result = ""
        if self.matrix < other.matrix:
            result = "Вторая матрица больше первой"
        elif self.matrix > other.matrix:
            result = "Первая матрица больше второй"
        else:
            result = "Матрицы равны"
        return result

    def __add__(self, other):
        result = []
        nums = []
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                summa = self.matrix[i][j] + other.matrix[i][j]
                nums.append(summa)
                if len(nums) == len(self.matrix[i]):
                    result.append(nums)
                    nums = []
        return result


if __name__ == "__main__":
    m1 = Matrix([[1, 2, 3], [4, 5, 6]])
    m2 = Matrix([[7, 8, 9], [1, 2, 3]])
    ms = m1 + m2
    print(ms)
    m3 = Matrix([[7, 8, 9], [1, 2, 3], [3, 4, 6]])
    m4 = Matrix([[7, 8, 9], [1, 2, 3]])
    mc = m4.transpose(m1)
    print(mc)
