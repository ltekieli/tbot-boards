import tbot


def test_uboot_info():
    tbot.ctx.teardown_if_alive(tbot.role.BoardLinux)
    with tbot.ctx.request(tbot.role.BoardUBoot) as ub:
        ub.exec0("version")
        ub.exec0("bdinfo")


def test_linux_info():
    with tbot.ctx.request(tbot.role.BoardLinux) as lnx:
        lnx.exec0("ip", "address")
        lnx.exec0("uname", "-a")
        lnx.exec0("cat", "/etc/os-release")
