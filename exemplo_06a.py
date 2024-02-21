import sys
import tkinter as tk

def main(): 
    root = tk.Tk()   
    root.title('Exemplo 06')
    widget = tk.Button(root, text='Hello event world', command=quit) 
    widget.pack()
    root.mainloop()

def quit():
    print('Hello, I must be going...') 
    #quit() #não sai pq esta chamando ela mesmo e o sys.exit esta comentado
    #acima a função quit que eu criei
    #root.quit() #não sai pq root não foi passado como argumento (não reconhece root)
    #acima a função quit do tkinter (root.quit)
    sys.exit() # por isso, somente o sys.exit() funciona

if __name__ == '__main__':
    main()
    print('Fim do programa')