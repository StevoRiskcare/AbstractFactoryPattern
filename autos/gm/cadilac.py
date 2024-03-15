from autos.abs_auto import AbsAuto


class Cadilac(AbsAuto):
    name = "Cadilac"

    def start(self):
        print("Starting {}".format(self.name))

    def stop(self):
        print("Stopping {}".format(self.name))