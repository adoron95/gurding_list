class names:
    """
    dict of names and id
    """
    def __init__(self):
        self.name_table={}

    def append(self,list_gard):
        for i in list_gard:
            self.name_table[i.id]=i.name

    def __str__(self):
        return str(self.name_table)