from builtins import *


class Singleton(object):
    def __new__(cls, *args, **kwds):
        it = cls.__dict__.get("__it__")
        if it is not None:
            return it
        cls.__it__ = it = object.__new__(cls)
        it.init(*args, **kwds)
        return it

    def init(self, *args, **kwds):
        pass


#Реализация была взята с сайта ниже, это официальная статья Гвидо ван Россума (создателя Python)
#https://www.python.org/download/releases/2.2/descrintro/#__new__