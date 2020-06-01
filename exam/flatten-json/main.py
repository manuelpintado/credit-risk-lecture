import logging
import fire
import utils
from utils import pretty_print

logger = logging.getLogger(__name__)


class Main(object):

    @pretty_print(logger)
    def show(self, filename):
        return utils.load_file(filename)

    @pretty_print(logger)
    def flatten(self, filename):
        return utils.flatten(utils.flatten_dict(utils.load_file(filename)))


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    fire.Fire(Main)
