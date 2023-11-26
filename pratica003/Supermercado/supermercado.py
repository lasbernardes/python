import string

def consultarPreco(List):
    #pass
    cod=input("Digite codigo para consulta: ")
    print(List)
    for line in List:
        
        print(line['cod'])
        try:
            if (cod==line['cod']):
                print(line["nome"])
                print(line["preco"])
                return
            #endif
        except:
            pass
        #endtry
    #endfor
    print("Produto não encontrado")
    
#enddef consultarPreco
def gerarCodigo(ultimo):
    ultimo = int(ultimo) + 1
    ultimo_str = str(ultimo)
    tamanho_atual = len(ultimo_str)
    
    if tamanho_atual < 13:
        zeros = '0' * (13 - tamanho_atual)  # Adiciona zeros à esquerda para alcançar 13 caracteres
        codigo = zeros + ultimo_str
        return str(codigo)
#enddef
#codigo = gerarCodigo(11)

def checarLista(List):
    if len(List)==0:
        return "0000000000000"
    else:
        return List[-1]["cod"]
    #endif
#enddef
def inserirProduto(List):
    #inserir codigo, nome, preco Produto"""
    
    #List=[]
    #codigo = gerarCodigo(11)
    while True:
        Prod={}
        #Prod["cod"]=gerarCodigo(List[-1]["cod"])
        Prod["cod"]=gerarCodigo(checarLista(List))
        #Prod["cod"] =input("Digite código:")
        print(Prod["cod"])
        aux=(input("Digite nome:"))
        Prod["nome"]=aux.title()
        #print(nome+"\n")
        Prod["preco"]=float(input("Digite preço:"))
        #print(preco+"\n")
        List.append(Prod)
        
        print(List)
        #print(List[0][1]+"\n")
        #print(List[0][2]+"\n")
        
        op=input("Inserir novo produto(s/n)? ")

        if (op.lower()=='n'):
            return List
            break
        #endif
#enddef inserirProduto

def excluirProduto(List):
    #pass
    cod=input("Digite codigo para exclusão: ")
    for line in List:
        try:
            if (cod==line["cod"]):
                List.remove(line)
                print("Produto removido com sucesso")
                return
            #endif 
        except:
            pass
        #endtry
    print("Produto não encontrado")
    
#enddef excluirProduto

def listarProduto(List):
    #pass
    cont=0
    mult=1
    for line in List:
        print(line["cod"]+"\t",end="")
        print(line["nome"]+"\t",end="")
        print(line["preco"])
        cont=cont+1

        if cont == 10*mult:
            mult=mult+1
            continuar = input("Digite para continuar (s/n): ")
            if continuar.lower() == 'n':
                break
            #enfif
        #endif
    #endfor
#enddef listarProduto



def main():
    List=[]
    List=inserirProduto(List)
    consultarPreco(List)
    excluirProduto(List)
    listarProduto(List)

#enddef main

if __name__ == "__main__":
    main()
#endif


