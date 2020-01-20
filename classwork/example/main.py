import logging

from settings import APP_LOG_LEVEL


logger = logging.getLogger(__name__)


def main():
    logger.info("Hello, World!")


if __name__ == "__main__":
    logging.basicConfig(level=APP_LOG_LEVEL)
    main()
