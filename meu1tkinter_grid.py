import tkinter as tk

def greeting():
    print('Hello stdout world!...')

def clean_func():
    e2.delete(0, tk.END)
    e1.delete(0, tk.END)
    print('Cleaned...')

def reply_func():
    e1.delete(0, tk.END)
    e1.insert(0, e2.get())
    print('Replyed...')


def main():

    '''root = tk.Tk()   
    root.title('Exemplo 09')
    win = tk.Frame(root)
    win.pack()
    tk.Entry(win).pack(side=tk.LEFT, expand=tk.YES)
    tk.Entry(win).pack(side=tk.RIGHT, expand=tk.YES)
    #tk.Label(win, text='Hello container world').pack(side=tk.TOP) 
    tk.Button(win, text='Reply', command=reply_func).pack(side=tk.LEFT, anchor='sw') 
    tk.Button(win, text='Clean', command=clean_func).pack(side=tk.RIGHT, anchor='se')
    tk.Button(win, text='Quit', command=root.quit).pack(side=tk.BOTTOM)
    
    root.mainloop()
'''
root = tk.Tk()
root.title('Reply - Clean - Quit')
#root.grid_columnconfigure(0, weight=1)  # Optional for horizontal centering
#root.grid_rowconfigure(0, weight=1)   # Optional for vertical centering
#root.geometry("800x600")

e1 = tk.Entry(root)
e2 = tk.Entry(root)
e1.grid(row=0, column=0,padx=10, pady=5)
e2.grid(row=0, column=1,padx=10, pady=5)
#e1.grid(row=0, column=0)
#e2.grid(row=0, column=1)

b1 = tk.Button(root, text='Reply', command=reply_func).grid(row=1, column=0, padx=10, pady=5)
    
tk.Button(root, text='Clean', command=clean_func).grid(row=1, column=1, padx=10, pady=5)
tk.Button(root, text='Quit', command=root.quit).grid(row=2, column=0, columnspan=2)

root.grid_columnconfigure(0, weight=1)  # Optional for horizontal centering
root.grid_rowconfigure(0, weight=1)   # Optional for vertical centering

root.mainloop()


if __name__ == '__main__':
    main()

