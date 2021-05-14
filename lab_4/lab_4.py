import sys
from collections import defaultdict

class CustomGraph():
    def __init__(self, w_matr = None, adj_matr = None):
        self.W_matrix = w_matr

        self.adj_matr = adj_matr

    def graph_printer(self):
        result = ''
        if self.W_matrix:
            matrix = self.W_matrix
        else:
            matrix = self.adj_matr

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                result += ' ' + str(matrix[i][j])
            result += '\n'
        
        print('--------- \n' + 'Given matrix:' + '\n' + result + '---------')
        
    def DFS(self, starter, target):
        N = len(self.adj_matr)
        nodes = [0 for i in range(N)]
        self.result = str(starter)
        self._rec_DFS(starter, target, nodes)
        print(self.result)

    def _rec_DFS(self, starter, target, nodes):
        self.result += ' ' + str(starter + 1)
        nodes[starter] = 1
        for i in range(target):
            if (self.adj_matr[starter][i] != 0 and nodes[i] == 0):
                self._rec_DFS(i, target, nodes)

    def BFS(self, node):
        graph = self._ajd_maker()
            
        visited = [False] * len(self.adj_matr)
        queue = []
        queue.append(node)
        visited[node] = True

        while queue:
            s = queue.pop(0)
            print(s, end = ' ')
            for i in graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

    def _ajd_maker(self):
        graph = defaultdict(list)
        for i in range(len(self.adj_matr)):
            for j in range(len(self.adj_matr[i])):
                if self.adj_matr[i][j] != 0:
                    graph[i].append(j)
        
        return(graph)

    def alg_Dijkstra(self, vershina, target):
        N = len(self.W_matrix)
        a = self.W_matrix
        d = [ sys.maxsize for _ in range(N)]
        v = [1 for _ in range(N)]
        d[vershina] = 0


        min_index = N
        min_way = sys.maxsize

        while min_index < (N + 1):
            min_index = N + 1
            min_way = sys.maxsize
            for i in range(N):
                if v[i] == 1 and d[i] < min_way:
                    min_way = d[i]
                    min_index = i
                
            if min_index != (N + 1):
                for i in range(N):
                    if a[min_index][i] > 0:
                        temp = min_way + a[min_index][i]
                        if temp < d[i]:
                            d[i] = temp

                v[min_index] = 0

        print("Кратчайшие расстояния до вершин:")
        result = ' '.join(str(el) for el in d )
        print(result)

        result = ''       

        vershiny = ['_' for i in range(N)] 
        end = target - 1
        vershiny[0] = end + 1
        weight_end = d[end]
        
        k = 1

        while end != vershina:
            for i in range(N):
                if a[i][end] != 0:
                    temp = weight_end - a[i][end]
                    if temp == d[i]:
                        weight_end = temp
                        end = i
                        vershiny[k] = i + 1
                        k += 1


        print('Вывод кратчайшего пути:')
        for i in range(N-1, -1, -1):
            if vershiny[i] != '_':
                result += ' ' + str(vershiny[i] - 1)
        print(result)

    def alg_Kruskala(self):
        N = len(self.W_matrix)
        result = []
        i = 0
        e = 0
        graph = sorted(self._w_maker(), key=lambda item: item[2])

        parent = []
        rank = []

        for node in range(N):
            parent.append(node)
            rank.append(0)
        
        while e < N - 1:
            u, v, w = graph[i]
            i = i + 1
            x = self._find(parent, u)
            y = self._find(parent, v)

            if x != y:
                e = e + 1
                result.append([u, v, w])
                self._union(parent, rank, x, y)
        
        minimalCost = 0
        print('Edges in the tree: ')
        for u, v, weight in result:
            minimalCost += weight
            print('%d - %d = %d' % (u, v, weight))
        print('Minimum spanning tree', minimalCost)

    def _find(self, parent, i):
        if parent[i] == i:
            return i
        return self._find(parent, parent[i])

    def _union(self, parent, rank, x, y):
        xroot = self._find(parent, x)
        yroot = self._find(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def _w_maker(self):
        graph = []
        for i in range(len(self.W_matrix)):
            for j in range(i, len(self.W_matrix[i])):
                if self.W_matrix[i][j] != 0:
                    graph.append([i, j, self.W_matrix[i][j]])

        return(graph)

# матрица весов ребер всех вершин графа 
w_matr1 = [[0, 7, 9, 0, 0, 14],
         [7, 0, 10, 15, 0, 0], 
         [9, 10, 0, 11, 0, 2], 
         [0, 15, 11, 0, 6, 0], 
         [0, 0, 0, 6, 0, 9],
         [14, 0, 2, 0, 9, 0]]

W1 = CustomGraph(w_matr = w_matr1)
W1.graph_printer()
W1.alg_Dijkstra(0, 5)

# матрица весов ребер всех вершин графа 
w_matr2 = [[0, 10, 6, 5],
            [0, 0, 0, 15],
            [0, 0, 0, 4],
            [0, 0, 0, 0]]


W2 = CustomGraph(w_matr = w_matr2)
W2.graph_printer()
W2.alg_Kruskala()


# матрица смежности
adj_matr = [[0, 1, 1, 0],
            [0, 0, 1, 0],
            [1, 0, 0, 1], 
            [0, 0, 0, 1]]

A = CustomGraph(adj_matr = adj_matr)
A.graph_printer()
print('DFS from node 0 to node 2')
A.DFS(0, 2)
print('BFS for the 2 node')
A.BFS(2)
