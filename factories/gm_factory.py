from autos.gm.cadilac import Cadilac
from autos.gm.camero import Camero
from autos.gm.spark import Spark
from factories.abs_factory import AbsFactory


class GMFactory(AbsFactory):
    @staticmethod
    def create_economy():
        return Spark()

    @staticmethod
    def create_sport():
        return Camero()

    @staticmethod
    def create_luxury():
        return Cadilac()