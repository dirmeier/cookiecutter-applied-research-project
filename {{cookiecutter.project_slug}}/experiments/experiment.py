import abc


class Experiment(metaclass=abc.ABCMeta):
    def __init__(self, FLAGS, workdir, run_name):
        pass