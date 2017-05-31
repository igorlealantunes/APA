class Min_heap:

    def __init__(self):
        self.list = [0]
        self.size = 0

    def fix_up(self, i):

        while i // 2 > 0: # enquanto nao chegar na raiz

            if self.list[i].v < self.list[i//2].v: # se pai for menor => troca
                self.swap(i, i//2)

            i = i // 2

    def insert(self, k):
        self.list.append(k)
        self.size = self.size + 1
        self.fix_up(self.size) # depois de inserir => corrige o heap a partir do valor inserido ate a raiz

    def fix_down(self, i): 

        while i * 2 < self.size: # enquanto estiver nos limites da arvore
            mc = self.min_child(i) # retorna o menor filho 

            if self.list[i].v > self.list[mc].v: # se pai manor que menor filho => troca
                self.swap(i, mc)

            i = mc


    def min_child(self,i): 
        if i * 2 + 1 > self.size: # se so tiver 1 filho
            return i * 2
        else: # com dois filhos
            if self.list[i*2].v < self.list[i*2+1].v:
                return i * 2
            else:
                return i * 2 + 1

    def pop_min(self):
        retval = self.list[1]
        self.list[1] = self.list[self.size]
        self.size = self.size - 1
        self.list.pop()
        self.fix_down(1) # refaz o heap 
        return retval

    def swap(self, i1, i2):
        temp = self.list[i1]
        self.list[i1] = self.list[i2]
        self.list[i2] = temp

    def build_heap(self, alist):
        i = len(alist) // 2
        self.size = len(alist)

        root = Heap_obj(0, "")

        self.list = [root] + alist[:]
        while (i > 0):
            self.fix_down(i)
            i = i - 1

    def print_heap(self):
        for i in range(1, len(self.list)):
            print self.list[i].to_string()

class Heap_obj :

    def __init__(self, v, k, f = None):
        self.v = v
        self.k = k
        self.father = f

    def to_string(self):
        return "V = " + str(self.v) + " K = " + str(self.k)
















