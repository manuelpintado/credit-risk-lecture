from typing import Callable, List, Optional

import numpy as np
import pandas as pd


class Amortization:

    def __init__(self, amount, rate, n):
        self.amount = amount
        self.rate = rate
        self.n = n

    @property
    def annuity(self):
        a = self.amount * self.rate / (1 - (1 + self.rate) ** (-self.n))
        return round(a, 2)

    def get_table(self):
        df = pd.DataFrame(index=range(0, self.n + 1), columns=["t", "BALANCE", "ANNUITY", "PRINCIPAL", "INTEREST"])
        df["t"] = range(0, self.n + 1)
        df.loc[0, "BALANCE"] = self.amount
        df.loc[1:, "ANNUITY"] = self.annuity
        for j in range(1, self.n + 1):
            df.loc[j, "INTEREST"] = round(df.loc[j - 1, "BALANCE"] * self.rate, 2)  # I_t = B_t-1 * i
            df.loc[j, "PRINCIPAL"] = round(df.loc[j, "ANNUITY"] - df.loc[j, "INTEREST"], 2)  # P_t = A_t - I_t
            df.loc[j, "BALANCE"] = round(df.loc[j - 1, "BALANCE"] - df.loc[j, "PRINCIPAL"], 2)  # B_t = B_t-1 - P_t
        return df

    def get_enriched_table(self, prob_of_default: float, loss_given_default: float) -> pd.DataFrame:
        df = self.get_table()
        df["IRR"] = 0
        df["EL"] = 0
        df["PROB"] = 0
        df.loc[0, "PROB"] = prob_of_default
        for i in range(1, self.n):
            df.loc[i, "PROB"] = round(df.loc[i - 1, "PROB"] * (1 - prob_of_default), 2)
        for i in range(0, self.n + 1):
            df.loc[i, "EL"] = round(prob_of_default * loss_given_default * df.loc[i, "BALANCE"], 2)
        df.loc[self.n, "PROB"] = round(1 - np.sum(df["PROB"]), 2)
        for i in range(1, self.n):
            cfs = [-self.amount] + [self.annuity] * i
            df.loc[i, "IRR"] = round(self.irr(cfs), 2)
        df.loc[self.n, "IRR"] = self.rate
        return df

    def expected_irr(self, prob_of_default: float, loss_given_default: float) -> float:
        df = self.get_enriched_table(prob_of_default, loss_given_default)
        irr_ind = np.array(df["IRR"])
        prob_ind = np.array(df["PROB"])
        exp_irr = irr_ind.dot(prob_ind)
        return round(exp_irr.item(), 2)

    @staticmethod
    def irr(cfs: list) -> float:
        res = np.roots(cfs[::-1])
        mask = (res.imag == 0) & (res.real > 0)
        if not mask.any():
            return np.nan
        res = res[mask].real
        rate = 1 / res - 1
        if rate.size == 1:
            return rate.item()
        return rate[np.argmin(np.abs(rate))].item()
