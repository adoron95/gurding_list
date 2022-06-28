import men
import operator

class justesTable:
    """

    """
    def __init__(self):
        self.table={}

    def append(self,gard,kept):
        """
        How many times each kept
        :param id:
        :return:
        """
        #id=gard.id
        #keept=gard.kept
        self.table[gard]=kept

    def sortVal(self):
        """
        :return:sorted dict by value
         """
        sort_j=sorted(self.table.items(), key=operator.itemgetter(1))
        self.table= dict(sort_j)

    def __str__(self):
        return str(self.table)

