import men
import constraints


class gard_cons_dict:
    """
    Represent all gards as dictionary
    """
    def __init__(self):
        self.gard_const_dic = {}
        #self.gard_const_dic= collections.defaultdict(g.Gard)

    def appendGard(self,gard,cons):
        """
        append gard to dict
        :param men class: id,name,phone,kept
        """
        id = gard.id
        co = cons#cons.cons1
        self.gard_const_dic[id] = co

    def __str__(self):

        #for k in self.gard_const_dic.items():

        return str(self.gard_const_dic)


    def deleteGard(self,gardId):
        """
        delete gard from dict
        :param gardId:
        :return:
        """
        del self.gard_const_dic[gardId.name]





