
class Permutation:
    def __init__(self,lista,permutacion):
        self.lista = lista.copy()
        self.permutacion = permutacion.copy()
    
    def isValid(self):
        for i in range(0,len(self.permutacion)):
            for j in range(0,len(self.permutacion)):
                if i == j:
                    continue
                if self.permutacion[i] == self.permutacion[j]:
                    return False
        return True

    def isFinal(self):
        if len(self.lista) == len(self.permutacion):
            return True
        else:
            return False

    def successors(self):
        self.succ = list()
        for i in self.lista:
            self.new_perm_list = self.permutacion.copy()
            self.new_perm_list.append(i)
            new_perm = Permutation(self.lista,self.new_perm_list)
            if new_perm.isValid():
                self.succ.append(new_perm)
        return self.succ

n = int(input(""))
x = list()
for i in range(0,n):
    x.append(input())

p = Permutation(x,list())
frontier = list()
frontier.append(p)
final_permutations = list()
while not len(frontier) == 0:
    np = frontier.pop()
    if np.isValid():
        if np.isFinal():
            final_permutations.append(np.permutacion)
        else:
            new_perm_list = np.successors()
            frontier = frontier + new_perm_list
for i in final_permutations:
    print(i)