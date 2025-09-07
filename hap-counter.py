from src.cli import parse_args
from src.logger import logger
from src.run import run


def main():
    args = parse_args()
    run(args)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.critical("something went horribly wrong: " + str(e), exc_info=True)
