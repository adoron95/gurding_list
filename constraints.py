class constraints:
    "represent the constraints on keeps dates "

    def __init__(self):
        """
        The constraints as list
        """
        self.cons1=[]
        self.cons2=[]

    def appendConstraints1(self, dates):
        """
        appened Constraints from user for the first monthe
        """
        self.cons1= self.cons1+dates


    def appendConstraints2(self, dates):
        """
       appened Constraints from user for the secunned mothe
        """
        self.cons2= self.cons2+dates
"""
class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method

"""