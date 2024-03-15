from autos.abs_auto import AbsAuto


class FordMustang(AbsAuto):
    name = "Ford Mustang"

    def start(self):
        print("Starting {}".format(self.name))

    def stop(self):
        print("Stopping {}".format(self.name))