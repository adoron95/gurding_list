class wishes:
    "represent the wishes of keeps dates "

    def __init__(self):
        """
        The constraints as list
        """
        self.wish1=[]
        self.wish2=[]

    def append_wish1(self, dates):
        """
        appened wishes from user for the first monthe
        """
        self.wish1= self.wish1+dates


    def append_wish2(self, dates):
        """
       appened wishes from user for the secunned mothe
        """
        self.wish2= self.wish2+dates