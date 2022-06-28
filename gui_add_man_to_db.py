import tkinter as tk
import json
from tkinter import *
from tkinter.messagebox import showinfo

fields = 'Last Name', 'First Name', 'phone'
class add_man:
    def __init__(self):
        self.man = {}
        self.key = " "

    def append(self, data):
        if self.check_data(data):
            self.key = data[0]
            self.man["fname"] = data[1]
            self.man["phone"] = data[2]

    def ave_kept(self):
        # Opening JSON file
        f = open('demo.json','r')
        data = json.load(f)

        sum_mid=0
        sum_end = 0
        for i in data:
            sum_mid+=data[i]["keptMid"]
            sum_end += data[i]["keptEnd"]

        len_data=len(data)   # dont do thing twice
        ave_mid=sum_mid//len_data
        ave_end=sum_end//len_data

        f.close()
        return ave_mid,ave_end


    #def note(self):
        """ callback when the login button clicked
    """

    #top = tk.Toplevel(root)
    #msg = f'ישנה בעיה בתוכן שהוזן אנא בדוק שוב'
    #showinfo(
     #   title='Information',
      #  message=msg
    #)

    def write_data(self):
        mid_ave,end_ave=self.ave_kept()
        data = {
            "fname": self.man["fname"],
            "phone": self.man["phone"],
            "keptMid": mid_ave,
            "keptEnd": end_ave
        }

        with open("demo.json", 'r+') as file:
            # First we load existing data into a dict.
            file_data = json.load(file)
            # Join new_data with file_data inside emp_details
            file_data[self.key]=data
            # Sets file's current position at offset.
            file.seek(0)
            # convert back to json.
            json.dump(file_data, file, indent=4)


    def check_data(self, data):
        flag = True
        for i in range(2):
            if data[i].isalpha() == False:
                flag = False

        if data[2].isalpha() == True:
            flag = False
        if not flag:
            print("Error")
            #note()
        return flag



def makeform(root, fields):
    """

    :param root: tk
    :param fields: f.l.name, phone
    :return: value from user
    """
    entries = []
    for field in fields:
        row = tk.Frame(root)
        lab = tk.Label(row, width=15, text=field, anchor='w')
        ent = tk.Entry(row)
        row.pack(side=tk.TOP, fill=tk.Y, padx=5, pady=5)
        lab.pack(side=tk.LEFT)
        ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
        entries.append((field, ent))
    return entries


def fetch(entries):
    # justice_midweek = jT.justesTable()
    add_man_to_data = add_man()
    data = []
    for entry in entries:
        field = entry[0]
        text = entry[1].get()
        data.append(text)
        print('"%s"' % (text))
    add_man_to_data.append(data)
    add_man_to_data.write_data()


def add_men_to_db():
    root = tk.Tk()
    root.geometry("400x200")
    root.resizable(False, False)
    root.title('הוספת שומר')
    signin = tk.Frame(root)
    signin.pack(padx=10, pady=10, fill='x', expand=False)

    label = tk.Label(signin, text="!!שים לב אתה מוסיף שומר לרשימת השמירה")
    label.pack(fill='y', expand=True)
    label = tk.Label(signin, text="טבלת הצדק תוזן באופן אוטומטי כממוצע")
    label.pack(fill='y', expand=True)

    ents = makeform(root, fields)
    root.bind('<Return>', (lambda event, e=ents: fetch(e)))
    b1 = tk.Button(root, text='אישור',
                   command=(lambda e=ents: fetch(e)))
    b1.pack(side=tk.LEFT, padx=5, pady=5)
    b2 = tk.Button(root, text='Quit', command=root.quit)
    b2.pack(side=tk.LEFT, padx=5, pady=5)
    root.mainloop()

