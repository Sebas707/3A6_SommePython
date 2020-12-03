import os

if os.name == 'posix':
    from setproctitle import setproctitle as spt  # noqa


def setproctitle(title: str) -> None:
    """Méthode DIRO pour setproctitle"""
    if os.name == 'posix':
        spt(title)
