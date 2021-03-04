
class CustomFunction:
    def __init__(self, x, y, h, m, customformula):
        self.xi = float(x)
        self.yi = float(y)
        self.h0 = float(h)
        self.m = int(m)
        self.formula = customformula

    def f(self, x, y):
        values = {
            'x': x,
            'y': y
            }
        return eval(self.formula, values)
    
    def set_integrate(self, form):
        self.integr_f = form
    
    def integr(self, x_to, y):
        
        h = self.h0 / self.m
        x = self.xi
        result = 0.0
        
        while x < x_to:
            x = x + h
            values_from = {
            'x': self.xi,
            'y': y
            }
            values_to = {
            'x': x,
            'y': y
            }
            result += eval(self.integr_f, values_from) - eval(self.integr_f, values_to) 

        return result      
     
    def RK4(self):
        h = self.h0/self.m
        x = x0 = self.xi
        y = self.yi


        list_of_x = [x]
        list_of_y = [y]

        for j in range(1, self.m+1):

            k1 = self.f(x, y)
            k2 = self.f(x+h/2, y+k1*h/2)
            k3 = self.f(x+h/2, y+h*k2/2)
            k4 = self.f(x+h, y+h*k3)

            y = y + (h/6) * (k1 + 2*k2 + 2*k3 + k4)
            x = x0 + j*h

            list_of_x.append(x)
            list_of_y.append(y)

        return list_of_x, list_of_y

    def predictor(self):
        l_x, l_y = self.RK4()
        h = self.h0/self.m
        
        for i in range(3, self.m):
            l_y[i+1] = l_y[i] + h/24 * (55*self.f(l_x[i], l_y[i]) - 59 * self.f(l_x[i-1], l_y[i-1]) +
            37 * self.f(l_x[i-2], l_y[i-2]) - 9* self.f(l_x[i-3], l_y[i-3]))
        
        return l_x, l_y

    def corrector(self):
        l_x, l_y = self.RK4()
        h = self.h0/self.m
        
        for i in range(2, self.m):
            l_y[i+1] = l_y[i] + h/24 * (9 * self.f(l_x[i+1], l_y[i+1]) + 19 * self.f(l_x[i], l_y[i]) - 5 * self.f(l_x[i-1], l_y[i-1]) + self.f(l_x[i-2], l_y[i-2]))
        
        return l_x, l_y

    def Adams(self):
        l_x, l_y = self.RK4()
        h = self.h0 / self.m

        for j in range(3, self.m):

            d_f1 = self.f(l_x[j], l_y[j]) - self.f(l_x[j-1], l_y[j-1])
            d_f2 = self.f(l_x[j], l_y[j]) -2*self.f(l_x[j-1], l_y[j-1]) + self.f(l_x[j-2], l_y[j-2])
            d_f3 = self.f(l_x[j], l_y[j]) -3 * self.f(l_x[j-1], l_y[j-1]) + 3 * self.f(l_x[j-2], l_y[j-2]) - self.f(l_x[j-3], l_y[j-3])

            l_y[j+1]= l_y[j] + ((h**2) * d_f1 / 2 + (h**3)*d_f2*5/12 + (h**4)*d_f3*3/8)

        return l_x, l_y 

    def approximate_metod(self):
        y0 = self.yi
        x = x0 = self.xi

        h = self.h0 / self.m 
        l_y = [y0]
        l_x = [x0]

        for i in range(1, self.m):
            x = x0 + i * h
            l_x.append(x) 
            y = y0 + self.integr(l_x[i-1], l_y[i-1])
            l_y.append(y) 

        return l_x,l_y




def show_result(returned_values):
    for i in range(len(returned_values[1])):
        if returned_values[0][i]:
            print('x results: {0:3.2f}|y results: {1:9.5f}'.format(returned_values[0][i], returned_values[1][i]))



u = CustomFunction(x=0, y=1, h = 1, m = 10, customformula='x**2-2*y')   # создание экземпляра класса, конструктор получает на вход начальные значения для x, y, шаг
                                                                        # хода и количество итераций, также принимает формулу в виде строки
print('Рассчет значения с помощью метода Рунге-Кутты 4-го порядка: ')
show_result(u.RK4())
print('\nРассчет значения с помощью метода прогноза и коррекции:\n Предиктор: ')
show_result(u.predictor())
print('\nРассчет значения с помощью метода прогноза и коррекции:\n Корректор: ')
show_result(u.corrector())
print('\nРассчет значения с помощью метода Адамса:')
show_result(u.Adams())
u.set_integrate('(x**3)/3-2*y')   # в функционале класса реализован сеттер для значения интеграла введенной функции
print('\nРассчет значения с помощью метода приближения значения: ')
show_result(u.approximate_metod())