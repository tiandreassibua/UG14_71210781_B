class Node: 
    def __init__(self,name, value):
        self._name = name 
        self._value = value

class Graph:
    def __init__(self):
        #constructor
        self._data = {}

    #menambah vertex (Node) baru ke dalam Graph
    def addVertex(self, name, value):
        # Membuat Node dari class Node yang menyimpan nama node dan nilai node
        node = Node(name, value)
        # jika node belum ada di self._data, maka tambahkan node tersebut ke self._data (graph)
        if name not in self._data.keys():
            # membuat set untuk relasi antar node (Edge), misal :
            # a = {b}
            # b = {c, d}
            # c = {g} 
            # dll
            setEdge = set()
            # untuk value dari key nama
            listData = [setEdge, node]
            # lalu kita simpan (misal) node dengan nama "a" sebagai Key
            # dengan value listData
            self._data[name] = listData
            # graph["a"] = [{""},Node("a",2)]

    def vertex(self):
        #mencetak seluruh vertex
        print("\n== Seluruh Node == ")
        # tulis kode Anda di sini
        for key in self._data.keys():
            print(f"{key}:{self._data[key][1]._value}")
        print()

    def addEdge(self, x, y):
        #menambah edge antara vertex x dan y
        # tulis kode Anda di sini
        if x in self._data.keys() and y in self._data.keys():
            self._data[x][0].add(y)
            self._data[y][0].add(x)
        print()

    def edge(self):
        print("== Seluruh Edge == ")
        # tulis kode Anda di sini
        listEdge = set()
        for key in self._data.keys():
            for item in self._data[key][0]:
                if key+item not in listEdge and item+key not in listEdge:
                    listEdge.add(key+item)

        edge = sorted(listEdge)
        for item in edge:
            print(item, end=' ')
            # print(f"{key} : {self._data[key][0]}")
        print("\n")
    
    # untuk pembacaan traversing bfs graph
    def bfs(self, node):
        # tulis kode Anda di sini
        print("Traversing BFS = ", end="")
        visited = []
        queue = []
        visited.append(node)
        queue.append(node)
        while queue:
            s = queue.pop(0)
            print(s, end=" ")
            for neighbour in self._data[s][0]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)
        print("\n")

graph = Graph()
graph.addVertex("a", 2)
graph.addVertex("b", 2)
graph.addVertex("c", 4)
graph.addVertex("d", 3)
graph.addVertex("e", 4)
graph.addVertex("f",3)
graph.addVertex("g", 3)
graph.addVertex("h", 3)

graph.addEdge('a', 'b')
graph.addEdge('b', 'c')
graph.addEdge('b', 'd')
graph.addEdge('c', 'g')
graph.addEdge('d', 'e')
graph.addEdge('f', 'h')
graph.addEdge('g', 'f')

graph.vertex()
graph.edge()
graph.bfs('a')
