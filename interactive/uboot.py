import tbot


def test():
    tbot.ctx.teardown_if_alive(tbot.role.BoardLinux)
    with tbot.ctx.request(tbot.role.BoardUBoot) as ub:
        ub.interactive()
