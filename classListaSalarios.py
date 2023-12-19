from classData import Data
from classAnaliseDados import AnaliseDados
from random import randint

class ListaSalarios(AnaliseDados):

    def __init__(self):
        super().__init__(type(float))
        self.__lista = []        

    def entradaDeDados(self, salario):
        self.__lista.append(salario)

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
        return '\n'.join(str(salario) for salario in self.__lista)
    
    def geralistaSalarios1(self, qtd=100, min=1320, max=13200):
        for i in range(qtd):
            self.entradaDeDados(randint(min, max))
        #end for
        return self.__lista
    #end def

def main():
    lista = ListaSalarios()
    #lista.
    lista.geralistaSalarios1()
    #print("lista: " + len(self.__lista))
    print(lista)
    print("Mediana: ",lista.mostraMediana(), end="\n")
    print("Menor: ", lista.mostraMenor(), end="\n")
    print("Maior: ", lista.mostraMaior(), end="\n")
    print(lista.listarEmOrdem())
#end def
if __name__ == "__main__":
    main()