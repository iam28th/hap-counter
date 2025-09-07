import os

from src.utils import now

OUTPUT = None


def get_default_output_path() -> str:
    if OUTPUT:
        return OUTPUT

    while True:
        filename = now().strftime("%m-%d_%H-%M-%S_pid") + str(os.getpid()) + ".tsv"
        if not os.path.exists(filename):
            return filename
