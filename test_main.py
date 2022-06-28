import json
import men as grd
import gardsCons as gd

import justesTable as jT
from order_midweek import ord_midweek as mid_ord
from order_weekend import ord_weekend as end_ord
import gui_delete_man_from_db as del_man
import gui_add_man_to_db as adding_man
import gui_request
import gui_ordering
import gard_wish as gw
import tkinter as tk
from tkinter import *
from tkinter import ttk

import gui_display_calendar

#test_main

def main_():
    def build_gard_dict_():
        with open("demo.json") as gards_data:
            data = gards_data.read()
            jdata = json.loads(data)


            for i in jdata:
                once = jdata[i]
                # name = i
                name = grd.men(i, once["fname"], once["phone"], once['keptMid'], once['keptEnd'])


                con_list, wish_list = once["dontWant"],once["want"]
                garDict.appendGard(name, con_list)
                gard_wish_dict.append_wish_Gard(name, wish_list)

                justice_midweek.append(name.id, name.kept_midweek)
                justice_weekend.append(name.id, name.kept_weekend)

            justice_midweek.sortVal()
            justice_weekend.sortVal()

    garDict = gd.gard_cons_dict()
    gard_wish_dict = gw.gard_wish_dict()
    justice_midweek = jT.justesTable()
    justice_weekend = jT.justesTable()

    build_gard_dict_()
    month, year = gui_ordering.input_date()
    oreder_midweek = mid_ord(justice_midweek, garDict, gard_wish_dict,month,year)
    oreder_weekend = end_ord(justice_weekend, garDict, gard_wish_dict,month,year)

    gui_display_calendar.display(oreder_midweek,oreder_weekend,month,year)





def gui_main():
    root = tk.Tk()
    root.geometry("600x300")
    root.resizable(False, False)
    root.title('רשימת שמירה בית חוגלה')
    signin = ttk.Frame(root)
    signin.pack(padx=10, pady=10, fill='x', expand=False)

    label = ttk.Label(signin, text="ברוכים הבאים לאתר השמירות של בית חוגלה")
    label.pack(fill='y', expand=True)

    login_button = ttk.Button(signin, text="הזן בקשות", command=gui_request.add_req)
    login_button.pack(fill='y', expand=True, pady=10)

    login_button = ttk.Button(signin, text="סדר רשימה", command=main_)
    login_button.pack(fill='y', expand=True, pady=10)

    add_gard_button = ttk.Button(signin, text="הוסף שומר", command=adding_man.add_men_to_db)
    add_gard_button.pack(fill='y', expand=True, pady=30)

    delete_gard_button = ttk.Button(signin, text="מחק שומר", command=del_man.delete_men_from_db)
    delete_gard_button.pack(fill='y', expand=True, pady=0)
    root.mainloop()


#    print("The Max val is " + str(maxHeap.extractMax()))
if __name__ == "__main__":
    gui_main()

