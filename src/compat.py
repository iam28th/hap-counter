import dataclasses
import sys


def dataclass(*args, slots=False, **kwargs):
    """Ignores slots argument if the Python version does not support it"""
    if sys.version_info >= (3, 10):
        kwargs["slots"] = slots

    return dataclasses.dataclass(*args, **kwargs)
