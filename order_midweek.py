from ordering import order
import calendar
import random

class ord_midweek(order):
    """
    Inheritance from order supposed to order midweek
    """
    def __init__(self,justice_midweek,gard_constraints,wishes_dict,month,year):
        """

        :param justice_midweek:
        :param gard_constraints:
        :param wishes_dict:

        """
        self.midweek = week_days(month,year)  # a dict
        super().__init__(justice_midweek,gard_constraints,wishes_dict,len(self.midweek))
        self.real_order()

    def __str__(self):
        return str(self.midweek)

    def real_order(self):
        """

        :return:
        """
        dead_dates = super().dead_lock(self.midweek)
        if  len(dead_dates) != 0:
            #ToDo random func
            a=1
        flag=True
        while flag:
            temp_order=n_queens(self.midweek,self.gards_id,self.gards_wish,self.gards_cons)
            if temp_order == False:
                temp_order = n_queens(self.midweek, self.gards_id,  self.gards_cons,self.gards_wish)
                #keys = self.gards_cons.keys()  # Python 3; use keys = d.keys() in Python
                #random.shuffle(keys)
                #{(key, self.gards_cons[key]) for key in keys}
            else: flag=False
        self.gards_final=temp_order
        super().add_oneDay_to_justes_table(self.gards_id,"keptMid")

def n_queens(month, id, wish, cons):
    """
    Algorithm structure:
    The heuristics try to combine the requests of the able and can not,
    so we will first examine the people with the most can not
    :param month:  { day: 0}
    :param id_list:
    :param wish: {id : listWish}
    :param cons: {id : listCons}
    :return:
    """
    id_list=id[:]
    loop = 0  # counting the num of loop while
    if len(id_list)!=len(month):
        return False
    while len(id_list) > 0:
        for day in month:
            if month[day] == 0:
                 for man in cons: # Heuristics provides a solution for people with the most problems before
                    if day in wish[man]:
                        month[day] = man
                        x = id_list.index(man)  # delete item fro all dict and list
                        id_list.pop(x)
                        cons.pop(man, None)
                        wish.pop(man, None)
                        break
                    elif day in cons[man] or loop < 2:
                        continue
                    else:               # after to loop the day no be in cons
                        month[day] = man
                        x = id_list.index(man)   # delete item fro all dict and list
                        id_list.pop(x)
                        cons.pop(man, None)
                        wish.pop(man, None)
                        break
        loop += 1
        if len(id_list)==0:
            break
    return month


def week_days(month,year):
    """
    dict represent the days mid-week's
    :return: midweek
    """

    c = calendar.TextCalendar(calendar.SUNDAY)
    v = c.monthdayscalendar(year, month)
    midweek = []
    for i in v:
        midweek += i[:-2]
    while 0 in midweek:
        zero = midweek.index(0)
        midweek.pop(zero)
    dictMidweek = {i: 0 for i in midweek}
    return dictMidweek