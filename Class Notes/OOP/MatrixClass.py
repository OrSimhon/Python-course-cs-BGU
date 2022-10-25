from VectorClass_Copy_DeepCopy import Vector


class Matrix:

    def __init__(self, vectors):
        self.vectors = vectors  # list of vectors

    def __repr__(self):
        """
        Matrix printing - vector in each row
        :return:
        """
        m = ""
        for vec in self.vectors:
            m = m + str(vec) + "\n"

        # .strip() remove leading and trailing whitespaces
        return m.strip()

    def __add__(self, other):
        return Matrix([self.vectors[i] + other.vectors[i] for i in range(len(self.vectors))])

    def __len__(self):
        return len(self.vectors)

    def __getitem__(self, item):
        return self.vectors[item]

    def transpose(self):
        vecs_lst = []
        for j in range(len(self[0])):  # Iterate over cols
            vec_lst = []
            for i in range(len(self)):  # Iterate over rows
                vec_lst.append(self[i][j])
            vecs_lst.append(Vector(vec_lst))
        return Matrix(vecs_lst)


# -------------------------- Matrix Class Functionality --------------------------
if __name__ == '__main__':
    vec1 = Vector([1, 2, 3])
    vec2 = Vector([4, 5, 6])
    mx = Matrix([vec1, vec2])
    print(mx.vectors)
    print("\n__repr__ method\n---------------")
    print(mx)

    print("\n__add__ method\n---------------")
    print(mx + mx)

    print("\ntranspose method\n---------------")
    print(mx.transpose())
