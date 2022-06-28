import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import json

fields = 'Last Name'

"""
def note(root):

    msg = f'ישנה בעיה בתוכן שהוזן אנא בדוק שוב'
    showinfo(
        title='Information',
        message=msg
    )
"""


def del_from_json(id):
    id = str(id)
    # if id.isalpha()==False:
    #    note()
    with open("demo.json", "r+") as jsonFile:
        data = json.load(jsonFile)
        flag = True
        for id_data in data:
            if id.lower() == id_data.lower():
                data.pop(id_data, None)
                flag = flag
                break
        # if flag:
        #   note()

        jsonFile.seek(0)  # rewind
        json.dump(data, jsonFile)
        jsonFile.truncate()



def makeform(root, fields):
    entries = []

    row = tk.Frame(root)
    lab = tk.Label(row, width=15, text='Last Name', anchor='w')
    ent = tk.Entry(row)
    row.pack(side=tk.TOP, fill=tk.Y, padx=5, pady=5)
    lab.pack(side=tk.LEFT)
    ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
    entries.append((ent))

    return ent


def fetch(entries):
    text = entries.get()
    print('"%s"' % (text))
    del_from_json(text)



def delete_men_from_db():
    root = tk.Tk()
    root.geometry("600x300")
    root.resizable(False, False)
    root.title('מחיקת שומר')
    signin = ttk.Frame(root)
    signin.pack(padx=10, pady=10, fill='x', expand=False)
    #
    id = tk.StringVar()

    label = ttk.Label(signin, text="!!שים לב אתה מוחק שומר מרשימת השמירהי")
    label.pack(fill='y', expand=True)
    label = ttk.Label(signin, text=":אנא הזן את שם המשפחה")
    label.pack(fill='y', expand=True)

    ents = makeform(root, fields)
    root.bind('<Return>', (lambda event, e=ents: fetch(e)))
    b1 = tk.Button(root, text='אישור',
                   command=(lambda e=ents: fetch(e)))
    b1.pack(side=tk.LEFT, padx=5, pady=5)
    b2 = tk.Button(root, text='Quit', command=root.quit)
    b2.pack(side=tk.LEFT, padx=5, pady=5)

    root.mainloop()
