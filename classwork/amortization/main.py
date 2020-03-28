import fire

from models import Amortization


class Main:
    @staticmethod
    def plot(amount: float, interest: float, n: int, show: bool, save: str = ''):
        amortization = Amortization(amount=amount, interest=interest, n=n)
        amortization.get_plot(show=show, save=save)

    @staticmethod
    def annuity(amount: float, interest: float, n: int):
        amortization = Amortization(amount=amount, interest=interest, n=n)
        print(amortization.annuity)

    @staticmethod
    def table(amount: float, interest: float, n: int, show: bool, save: str = ''):
        amortization = Amortization(amount=amount, interest=interest, n=n)
        amortization.get_table(show=show, save=save)


if __name__ == "__main__":
    fire.Fire(Main)
