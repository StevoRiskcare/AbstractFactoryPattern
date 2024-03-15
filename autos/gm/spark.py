from autos.abs_auto import AbsAuto


class Spark(AbsAuto):
    name = "Spark"

    def start(self):
        print("Starting {}".format(self.name))

    def stop(self):
        print("Stopping {}".format(self.name))