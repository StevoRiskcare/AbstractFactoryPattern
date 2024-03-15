from autos.ford.ford_fiesta import FordFiesta
from autos.ford.ford_lincoln import FordLincoln
from autos.ford.ford_mustang import FordMustang
from factories.abs_factory import AbsFactory


class FordFactory(AbsFactory):
    @staticmethod
    def create_economy():
        return FordFiesta()

    @staticmethod
    def create_sport():
        return FordMustang()

    @staticmethod
    def create_luxury():
        return FordLincoln()