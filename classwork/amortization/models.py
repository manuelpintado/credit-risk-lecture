import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class Amortization:

    def __init__(self, amount: float, interest: float, n: int):
        self.amount = amount
        self.interest = interest
        self.n = n

    @property
    def annuity(self) -> float:
        return self.amount / ((1 - (1 + self.interest) ** -self.n) / self.interest)

    def get_table(self, show: int = 0, save: str = '') -> pd.DataFrame:
        table = pd.DataFrame(columns=['t', 'B', 'P', 'I', 'A'])
        table.t = np.arange(0, self.n + 1).astype(int)
        table.A[1:] = self.annuity
        next_principal = 0
        for i in table.index:
            if i == 0:
                table.loc[i, 'B'] = self.amount
            else:
                table.loc[i, 'I'] = table.B.iloc[i - 1] * self.interest
                table.loc[i, 'P'] = self.annuity - table.I.iloc[i]
                table.loc[i, 'B'] = table.B.iloc[i - 1] - table.P.iloc[i]
        if show > 0:
            pd.options.display.float_format = '${:,.2f}'.format
            print(table.head(show))
        if save:
            table.to_csv(save)
        return table

    def get_plot(self, show: bool = False, save: str = ''):
        df = self.get_table()
        # df = pd.read_cvs('example.csv')
        plot = df.plot.bar(x='t', y=['P', 'I'], stacked=True)
        plt.title('Amortization Payment')
        plt.ylabel('$$$')
        plt.grid()
        fig = plot.get_figure()

        if show:
            plt.show()
        if save:
            fig.savefig(save)
        return fig
