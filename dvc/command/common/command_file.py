import yaml

from dvc.state_file import StateFileBase


class CommandFile(StateFileBase):
    MAGIC = 'DVC-Command-State'
    VERSION = '0.1'

    PARAM_CMD = 'cmd'
    PARAM_OUT = 'out'
    PARAM_REG = 'reg'
    PARAM_DEPS = 'deps'
    PARAM_LOCK = 'locked'

    def __init__(self, cmd, out, reg, deps, locked, fname):
        self.cmd = cmd
        self.out = out
        self.reg = reg
        self.deps = deps
        self.locked = locked
        self.fname = fname

    @property
    def dict(self):
        data = {
            self.PARAM_CMD: self.cmd,
            self.PARAM_OUT: self.out,
            self.PARAM_REG: self.reg,
            self.PARAM_DEPS: self.deps,
            self.PARAM_LOCK: self.locked
        }

        return data

    def dumps(self):
        return yaml.dump(self.dict)

    def dump(self, fname):
        with open(fname, 'w+') as fd:
            fd.write(self.dumps())

    @staticmethod
    def loadd(data, fname=None):
        return CommandFile(data.get(CommandFile.PARAM_CMD, None),
                           data.get(CommandFile.PARAM_OUT, None),
                           data.get(CommandFile.PARAM_REG, None),
                           data.get(CommandFile.PARAM_DEPS, None),
                           data.get(CommandFile.PARAM_LOCK, None),
                           fname)

    @staticmethod
    def load(fname):
        return CommandFile._load(fname, CommandFile, fname)