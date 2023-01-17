import tbot
from config.powerstrip import PowerStrip
from tbot.machine import board, connector, linux


class Visionfive2Board(connector.ConsoleConnector, board.PowerControl, board.Board):
    baudrate = 115200
    serial_port = "/dev/ttyUSB0"

    def connect(self, mach):
        return mach.open_channel("picocom", "-b", str(self.baudrate), self.serial_port)

    def power_strip(self):
        return PowerStrip("192.168.10.20", 5000, "1", 0)

    def poweron(self):
        self.power_strip().cycle(Visionfive2Board.powercycle_delay)

    def poweroff(self):
        self.power_strip().off()

    powercycle_delay = 2.0


class Visionfive2Uboot(board.Connector, board.UBootShell):
    name = "u-boot"
    prompt = "StarFive # "


class Visionfive2Linux(board.LinuxUbootConnector, board.LinuxBootLogin, linux.Ash):
    username = "root"
    password = None
    uboot = Visionfive2Uboot


def register_machines(ctx):
    ctx.register(Visionfive2Board, tbot.role.Board)
    ctx.register(Visionfive2Uboot, tbot.role.BoardUBoot)
    ctx.register(Visionfive2Linux, tbot.role.BoardLinux)
