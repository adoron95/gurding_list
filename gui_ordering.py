import tkinter as tk
import json

def convert_input_to_int_list(list):
    """
    use for valid data
    :param list:
    :return:
    """
    list = list.split(',')
    new_list=[]
    for i in range(0, len(list)):
        if list[i].isnumeric() and int(list[i])not in new_list:
            new_list.append(int(list[i]))

    #new_list = list(map(int, new_list))
    return new_list

def check_validaiation(lst1,lst2):
    """

    :param lst1:
    :param lst2:
    :return:
    """
    if len(lst1)==0 or len(lst2)==0:
        return False
    for num in lst1:
        if num in lst2:
            return True
    return False

def master(Lname):
    """
    window for input data
    :param Lname:
    :return: tow lists
    """
    my_var = tk.StringVar()
    my_var1 = tk.StringVar()
    mast = tk.Tk()
    mast.title(Lname)

    tk.Label(mast, text="לא רוצה").grid(row=0)
    tk.Label(mast, text="רוצה").grid(row=1)

    e1 = tk.Entry(mast,textvariable=my_var)
    e2 = tk.Entry(mast,textvariable=my_var1)

    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)

    tk.Button(mast,
              text='יציאה'

              ,command=mast.quit
              #,command=master.destroy
                ).grid(row=3,
                                        column=2,
                                        sticky=tk.W,
                                        pady=4)


    mast.mainloop()
    dontWant = e1.get()
    want = e2.get()


    #return my_var1.get(),my_var.get()
    return dontWant, want,mast

def input_date():
    """
    input from user the month and year
    :return: int month and year
    """
    master = tk.Tk()
    master.title("חודש ושנה")

    tk.Label(master, text="חודש").grid(row=0)
    tk.Label(master, text="שנה (לדוג' 2022)").grid(row=1)

    e1 = tk.Entry(master)
    e2 = tk.Entry(master)

    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)

    tk.Button(master,
              text='Quit',
              command=master.quit).grid(row=3,
                                        column=2,
                                        sticky=tk.W,
                                        pady=4)


    master.mainloop()
    month = e1.get()
    year = e2.get()
    return int(month),int(year)


