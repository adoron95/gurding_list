class men:
    """
    Represent a single gard.
    """
    def __init__(self,id,name,phone,kepMid,kepEnd):

        self.id=id
        self.name=name
        self.phone=phone
        self.kept_midweek=kepMid
        self.kept_weekend=kepEnd

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


    def plusKept_midweek(self):
        """
        if his garde + to justes table
        """
        self.kept_midweek+=1


    def minusKept_midweek(self):
        """
        if using in force oppertion is uptate the justes table
         """
        self.kept_midweek-=1


"""
class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)
"""