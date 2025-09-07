import datetime
import os


def now():
    return datetime.datetime.now()


def next_or_none(iterator):
    try:
        return next(iterator)
    except StopIteration:
        return None
