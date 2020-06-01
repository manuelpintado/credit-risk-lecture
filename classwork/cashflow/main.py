import fire
import logging
from models import CashFlow
from utils import pretty_print


logger = logging.getLogger(__name__)


class Main(object):


    @staticmethod
    @pretty_print(logger)
    def future_value(amount, rate, t):
        cf = CashFlow(amount=amount, t=0)
        return cf.shift(t=t, ir=rate)

    @staticmethod
    @pretty_print(logger)
    def present_value(amount, rate, t):
        cf = CashFlow(amount=amount, t=t)
        return cf.present_value(ir=rate)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    fire.Fire(Main)
