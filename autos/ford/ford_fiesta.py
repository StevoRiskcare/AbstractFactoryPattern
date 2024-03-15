from autos.abs_auto import AbsAuto


class FordFiesta(AbsAuto):
    name = "Ford Fiesta"

    def start(self):
        print("Starting {}".format(self.name))


    def stop(self):
        print("Stopping {}".format(self.name))