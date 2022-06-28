import men



class gard_wish_dict:
    """
    Represent all gards as dictionary with ther wish
    """
    def __init__(self):
        self.id_wish_dict = {}

    def append_wish_Gard(self,gard,wis):
        """
        append gard to dict
        :param men class: id,name,phone,kept
        """
        id = gard.id
        wish = wis   #.wish1
        self.id_wish_dict[id] = wish

    def __str__(self):

        #for k in self.gard_const_dic.items():

        return str(self.id_wish_dict)


    def delete_wish_Gard(self,gardId):
        """
        delete gard from dict
        :param gardId:
        :return:
        """
        del self.id_wish_dict[gardId.name]
