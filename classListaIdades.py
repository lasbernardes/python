from classData import Data
from classAnaliseDados import AnaliseDados
from random import randint
import timeit

class ListaIdades(AnaliseDados):
    
    def __init__(self):
        super().__init__(type(int))
        self.__lista = []        

    def entradaDeDados(self, idade):
        self.__lista.append(idade)

    def mostraMediana(self):
        self.__lista.sort()
        mediana_index = len(self.__lista) // 2
        mediana = self.__lista[mediana_index]
        return mediana

    def mostraMenor(self):
        menor = min(self.__lista)
        return menor

    def mostraMaior(self):
        maior = max(self.__lista)
        return maior

    def listarEmOrdem(self):
        lista_ordenada = sorted(self.__lista)
        return lista_ordenada

    def __iter__(self):
        return iter(self.__lista)

    def __str__(self):
        return '\n'.join(str(idade) for idade in self.__lista)
    
    def geraListaIdades1(self, qtd=100, min=18, max=65):
        for i in range(qtd):
            self.entradaDeDados(randint(min, max))
        #end for
        return self.__lista
    #end def
'''
    #class ListaIdade:
    def __init__(self, idades):
        self.idades = idades

    def geraListaIdades(self, qtd, min=18, max=65):
        idades = []
        print("gerando lista de idades...")
        for _ in range(qtd):
            idade = randint(min, max)
            idades.append(idade)
        return ListaIdades(idades)
    '''
def main():
    lista = ListaIdades()
    lista.geraListaIdades1(5000,18,65)
    #lista.
    #lista=ListaIdades.geraListaIdades(5000,18,65)
    #print("lista: " + len(self.__lista))
    #timeit.timeit('lista.mostraMediana()')
    #lista.mostraMediana()
    
    print(lista)
    print("Mediana: ", lista.mostraMediana(), end="\n")
    print("Menor: ", lista.mostraMenor(), end="\n")
    print("Maior: ", lista.mostraMaior(), end="\n")
    print(lista.listarEmOrdem())
#end def

if __name__ == "__main__":
    main()