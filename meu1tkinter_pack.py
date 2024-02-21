import tkinter as tk

def greeting():
    print('Hello stdout world!...')

def clean_func(e2,e1):
    e2.delete(0, tk.END)
    e1.delete(0, tk.END)
    print('Cleaned...')

def reply_func(e2,e1):
    e1.delete(0, tk.END)
    e1.insert(0, e2.get())
    print('Replyed...')

def quit_func(b3):
    print('Quited...')
    b3.quit()


def main():

    root = tk.Tk()   
    root.title('Reply - Clean - Quit')
    win = tk.Frame(root)
    win.pack()
    
    e1 = tk.Entry(win)
    e1.pack(side="left", fill="x", expand=True)
    e2 = tk.Entry(win)
    e2.pack(side="right", fill="x", expand=True)

    b1 = tk.Button(win, text='Reply', command=lambda: reply_func(e2,e1))
    b1.pack(side="left", fill="both", expand=True) 
    b2 = tk.Button(win, text='Clean', command=lambda: clean_func(e2,e1))
    b2.pack(side="left", fill="both", expand=True)
    b3 = tk.Button(win, text='Quit', command=lambda: quit_func(b3))
    b3.pack(side="bottom", fill="none", expand=True, anchor="center")
    
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
'''

if __name__ == '__main__':
    main()

