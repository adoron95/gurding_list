import tkinter as tk
from tkinter import *
from tkinter import ttk
import json
from tkinter import messagebox
import gui_ordering

import test_main


def warning():
    messagebox.showwarning("warning", "בקשתך לא התקבלה\nישנה בעיה בתוכן שהוזן")





def makerom(root):
    temp = []
    with open("demo.json", "r+") as jsonFile:
        data = json.load(jsonFile)
        for id_data in data:
            temp.append(id_data)
        jsonFile.close()

    # cmb = ttk.Combobox(root, width="10", values=("prova", "ciao", "come", "stai"))
    personChoosen = ttk.Combobox(root, width=27, values=tuple(temp))

    # Adding combobox drop down list
    # personChoosen['values']=tuple(temp)
    def checkcmbo():
        name = personChoosen.get()
        f = open('demo.json', 'r+')
        data = json.load(f)
        con_, wish_ ,mast= gui_ordering.master(name)
        mast.destroy()
        con_list = gui_ordering.convert_input_to_int_list(con_)
        wish_list = gui_ordering.convert_input_to_int_list(wish_)
        valid_input = gui_ordering.check_validaiation(con_list, wish_list)
        if not valid_input:
            data[name]["want"] = wish_list
            data[name]["dontWant"] = con_list
            f.seek(0)
            # convert back to json.
            json.dump(data, f, indent=4)
            f.truncate()
        else: warning()
        f.close()

    personChoosen.current(0)
    personChoosen.pack()
    btn = ttk.Button(root, text="הכנס בקשה", command=checkcmbo)
    btn.pack()

def restart():
    f = open('demo.json', 'r+')
    data = json.load(f)
    for name in data:

        data[name]["want"] = []
        data[name]["dontWant"] = []
    f.seek(0)
    json.dump(data, f, indent=4)
    f.truncate()
    f.close()
    messagebox.showinfo("showinfo", "בקשתך התקבלה")


def add_req():
    root = tk.Tk()
    root.geometry("600x300")
    root.resizable(False, False)
    root.title('בקשות שמירה')
    signin = tk.Frame(root)
    signin.pack(padx=10, pady=10, fill='x', expand=False)

    #root.bind('<Return>', (lambda event, e=ents: fetch(e)))
    b1 = tk.Button(root, text='סדר רשימה',command=test_main.main_)#,
                # command=(lambda e=ents: fetch(e)))
    b1.pack(side=tk.LEFT, padx=5, pady=5)
    b2 = tk.Button(root, text='אפס בקשות', command=restart)  # ,
    # command=(lambda e=ents: fetch(e)))
    b2.pack(side=tk.RIGHT, padx=5, pady=5)
    b3 = tk.Button(root, text='Quit', command=root.quit)
    b3.pack(side=tk.RIGHT, padx=5, pady=5)
    ents = makerom(root)
    # Adding combobox drop down list
    # personChoosen['values']=tuple(temp)

    root.mainloop()
