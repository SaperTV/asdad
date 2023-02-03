from mozg import Mozg
from serce import Serce
from ploca import Ploca
from nerki import Nerki
from brzuch import Brzuch
from watroba import Watroba


class Czlowiek():
    def __init__(self) -> None:
        self.__mozg = Mozg()
        self.__serce = Serce()
        self.__ploca = Ploca()
        self.__nerki = Nerki()
        self.__brzuch = Brzuch()
        self.__watroba = Watroba()
    
    def robimozg(self):
        self.__mozg.robimozg()

    def robiserce(self):
        self.__serce.robiserce()

    def robiploca(self):
        self.__ploca.robiploca()

    def robinerki(self):
        self.__ploca.robiploca()

    def robibrzuch(self):
        self.__brzuch.robibrzuch()

    def robiwatroba(self):
        self.__watroba.robiwatroba()