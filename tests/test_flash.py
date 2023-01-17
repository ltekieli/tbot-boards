import pytest
import tbot
from config.tftp import TftpServer


@pytest.fixture(scope="module")
def tftp_server(request):
    tftp_root = request.config.option.tftp_root
    assert tftp_root
    with TftpServer(tftp_root, 9069):
        yield


def setup_network(ub):
    ub.env("ipaddr", "192.168.10.110")
    ub.env("serverip", "192.168.10.100")
    ub.env("ethact", "eth0")
    ub.exec0("ping", "192.168.10.100")


def test_flash_sdcard(tftp_server):
    tbot.ctx.teardown_if_alive(tbot.role.BoardLinux)
    with tbot.ctx.request(tbot.role.BoardUBoot) as ub:
        setup_network(ub)
        ub.exec0("tftpboot", "0x82000000", "sdcard.img")
        ub.exec0("setexpr", "blocks", ub.env("filesize"), "/", "0x200")
        ub.exec0("mmc", "dev", "1")
        ub.exec0("mmc", "write", ub.env("fileaddr"), "0", ub.env("blocks"))


def test_flash_spi_nor(tftp_server):
    tbot.ctx.teardown_if_alive(tbot.role.BoardLinux)
    with tbot.ctx.request(tbot.role.BoardUBoot) as ub:
        setup_network(ub)
        ub.exec0("tftpboot", "0x82000000", "spi-nor.img")
        ub.exec0("sf", "probe")
        ub.exec0("sf", "update", "0x82000000", "0x0", ub.env("filesize"))
