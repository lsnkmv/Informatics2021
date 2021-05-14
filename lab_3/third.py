class CustomMatrix():

    def __init__(self, A_matr, B_matr):
        self.A_matrix = A_matr
        self.B_matrix = B_matr
        self.answers_Gauss = None
        self.answers_Thomas = None


    def _transform_matrix(self, Amatrix, Bmatrix, count):
        """ 
        Функция берет на вход матрицы коэффициентов и матрицы результата,
        и приводит их к ступенчатому виду (прямой ход)
        """
        for row in range(count-1):
            while (Amatrix[row][row] == 0):
                Amatrix[row], Amatrix[row+1] = Amatrix[row+1], Amatrix[row]

            for el in range(row+1, count):
                koeff = Amatrix[el][row]/Amatrix[row][row]

                for j in range(0, count):
                    Amatrix[el][j] -= koeff * Amatrix[row][j]
                
                Bmatrix[el] -= koeff * Bmatrix[row]
        return Amatrix, Bmatrix

    def _x_finder(self, Amatrix, Bmartix):
        """
        Функция реализует обратный ход алгоритма Гаусса
        """
        list_of_x = [0 for i in range(len(Amatrix))]
        for i in range(len(Amatrix)-1, -1, -1):
            s = 0
            for j in range(0, len(Amatrix)):
                s += Amatrix[i][j]*list_of_x[j]
            list_of_x[i] = (Bmartix[i]-s)/Amatrix[i][i]
        return list_of_x            

    def Gauss_algorithm(self):
        Amatrix = self.A_matrix
        Bmatrix = self.B_matrix

        Amatrix, Bmatrix = self._transform_matrix(Amatrix, Bmatrix, len(self.A_matrix))
        self.answers_Gauss = self._x_finder(Amatrix, Bmatrix)


    def Thomas_algorithm(self):
        """
        Функция реализует метод прогонки
        """
        Amatrix = self.A_matrix
        Bmatrix = self.B_matrix
        count = len(Amatrix)
        
        # Расчет коэффициентов для первой строки матрицы
        temp = Amatrix[0][0] 
        Akoeff = [-Amatrix[0][1]/temp]
        Bkoeff = [Bmatrix[0]/temp]
        list_of_x = [1 for i in range(count)] # для удобства итерации по массиву ответов,
                                            # массив ответов заполняется единицами
        for i in range(1, count-1):
            temp = Amatrix[i][i] + Amatrix[i][i-1] * Akoeff[i-1]
            Akoeff.append(-Amatrix[i][i+1]/temp)
            Bkoeff.append((Bmatrix[i] - Akoeff[i]*Bkoeff[i-1])/temp)
        
        # Расчет коэффициентов для последней строки матрицы
        temp = Amatrix[-1][-1] + Amatrix[-1][-2]*Akoeff[-1]
        Bkoeff.append((Bmatrix[-1]-Amatrix[-1][-2]*Bkoeff[-1])/temp)

        # Этап обратного хода
        list_of_x[-1] = (Bkoeff[-1])
        for i in range(count-2, -1, -1):
            list_of_x[i] = Akoeff[i] * list_of_x[i+1] + Bkoeff[i]  
        
        self.answers_Thomas = list_of_x

    def print_info(self):
        """
        Функция для вывода результатов рассчетв
        """
        print('\tThe equation:')
        for i in range(len(self.B_matrix)):
            print('{0:5.2f} {1:5.2f} {2:5.2f} {3:5.2f} | {4:5.2f}'.format(*self.A_matrix[i], self.B_matrix[i]))

        if self.answers_Gauss:
            print('The solution, which was found with Gauss algorithm')
            for answ in self.answers_Gauss:
                print('{:5.2f}'.format(answ))
        else:
            print('To see solution, which was found with Gauss algorithm, you should make a call to Gauss_algorithm method')
        if self.answers_Thomas:
            print('The solution, which was found with Thomas algorithm')
            for answ in self.answers_Thomas:
                print('{:5.2f}'.format(answ))
        else:
            print('To see solution, which was found with Thomas algorithm, you should make a call to Thomas_algorithm method')

matrix1 = [[4, 1, 1, 2],
            [1, 3, 2, -1],
            [2, -1, 5, 3],
            [4, 5, 4, -4]]

answers1 = [2, 2, -1, 8]

example1 = CustomMatrix(matrix1, answers1)
example1.Gauss_algorithm()
example1.print_info()


matrix2 = [
    [2, 2, 0, 0],
    [-1, 2, -0,5, 0],
    [0, 1, -3, -1],
    [0, 0, 1, 2]
]
answers2 = [1, 0, 2, 2]

example2 = CustomMatrix(matrix2, answers2)
example2.Thomas_algorithm()
example2.print_info()

