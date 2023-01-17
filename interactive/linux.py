import tbot


def test():
    with tbot.ctx.request(tbot.role.BoardLinux) as lnx:
        lnx.interactive()
