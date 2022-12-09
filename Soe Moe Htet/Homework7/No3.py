class LinearEquation:
    def __init__(self, a, b, c, d, e, f):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f

    def get_a(self, a):
        return self.__a

    def get_b(self, b):
        return self.__b

    def get_c(self, c):
        return self.__c

    def get_d(self, d):
        return self.__d

    def get_e(self, e):
        return self.__e

    def get_f(self, f):
        return self.__f

    def isSolvable(self):
        if( (self.__a * self.__d) - (self.__b* self.__c) !=0 ):
            return True
        else:
            return False

    def getX(self):
        top =( self.__e * self.__d) - (self.__b * self.__f)
        bottom = (self.__a * self.__d) - (self.__b * self.__c)
        return top / bottom

    def getY(self):
        top =( self.__a * self.__f) - (self.__e * self.__c)
        bottom = (self.__ * self.__d) - (self.__b * self.__c)
        return top / bottom

