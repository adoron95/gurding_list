from ordering import order
import calendar
import random


class ord_weekend(order):
    """
    Inheritance from order supposed to order midweek
    """

    def __init__(self, justice_weekend, gard_constraints, wishes_dict,month,year):
        """

        :param justice_weekend:
        :param gard_constraints:
        :param wishes_dict:
        """
        self.weekend = weekend_days(month,year)
        super().__init__(justice_weekend, gard_constraints, wishes_dict, 2 * len(self.weekend))
        self.real_order()

    def __str__(self):
        return str(self.weekend)

    def real_order(self):

        dead_dates = self.dead_lock(self.weekend)
        if len(dead_dates) != 0:
            # ToDo random func
            a = 1
        flag = True
        while flag:
            temp_order = n_queens_weekend(self.weekend, self.gards_id, self.gards_wish, self.gards_cons)
            if temp_order == False:
                temp_order = n_queens_weekend(self.weekend, self.gards_id, self.gards_cons, self.gards_wish)
                # keys = self.gards_cons.keys()  # Python 3; use keys = d.keys() in Python
                # random.shuffle(keys)
                # {(key, self.gards_cons[key]) for key in keys}
            else:
                flag = False
        self.gards_final = temp_order
        super().add_oneDay_to_justes_table(self.gards_id, "keptEnd")


def n_queens_weekend(month, id, wish, cons):
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
    id_list = id[:]
    loop = 0  # counting the num of loop while
    while len(id_list) > 0:
        for day in month:
            if len(month[day]) < 2:
                for man in cons:
                    # Heuristics provides a solution for people with the most problems before
                    if day in wish[man]:
                        month[day].append(man)
                        x = id_list.index(man)
                        id_list.pop(x)
                        cons.pop(man, None)
                        wish.pop(man, None)
                        break
                    elif day in cons[man] or loop < 1:
                        continue
                    else:  # after to loop the day no be in cons
                        month[day].append(man)
                        x = id_list.index(man)
                        id_list.pop(x)
                        cons.pop(man, None)
                        wish.pop(man, None)
                        break
        loop += 1
        if len(id_list) == 0:
            break
    return month


def weekend_days(month,year):
    """
    List represent the days weekend's
    :return: weekend
    """

    c = calendar.TextCalendar(calendar.SUNDAY)
    v = c.monthdayscalendar(year,month)
    weekend = []
    for i in v:
        weekend += i[5:]
    while 0 in weekend:
        z = weekend.index(0)
        weekend.pop(z)
    dictWeekend = {i: [] for i in weekend}
    return dictWeekend
