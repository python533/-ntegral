import numpy

class integral:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def metod(self,coz):
        birinci_denklem = (self.x, self.y)
        ikinci_denklem = (self.y, self.x)

        uygula =coz((birinci_denklem, ikinci_denklem), (x, y))

        for key in uygula:
            print(f"{key} = {uygula[key]}")



