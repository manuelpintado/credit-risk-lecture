import fire
import logging

from utils import timeit

logger = logging.getLogger(__name__)


class Main(object):

    def _get_element(self, i, j):
        pass

    def _naive_implementation(self, level, index=0):
        print("Missing implementation!")

    @timeit(logger)
    def pascal_triangle(self, level: str, start: int = 0):
        self._naive_implementation(level, index=start)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    fire.Fire(Main)
