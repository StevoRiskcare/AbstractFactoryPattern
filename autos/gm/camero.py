from autos.abs_auto import AbsAuto


class Camero(AbsAuto):
    name = "Camero"

    def start(self):
        print("Starting {}".format(self.name))

    def stop(self):
        print("Stopping {}".format(self.name))