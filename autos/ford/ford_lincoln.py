from autos.abs_auto import AbsAuto


class FordLincoln(AbsAuto):
    name = "Ford Lincoln"

    def start(self):
        print("Starting {}".format(self.name))

    def stop(self):
        print("Stopping {}".format(self.name))