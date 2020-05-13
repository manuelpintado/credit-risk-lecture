import fire
import logging

from settings import EXPECTED_RATE_LOG_LEVEL
from models.drive import (
    ConfigTable,
    RateValue,
    RequestValue,
    ResultTable
)
from models.finance import Amortization
from utils import setup, search
import pandas as pd

logger = logging.getLogger(__name__)


class Main:

    @staticmethod
    def setup():
        setup()

    @staticmethod
    def loan_request_local(loan_amount, loan_marr, loan_terms, probability_of_default,
                           loss_given_default, client_min_rate, client_max_rate,
                           search_samples, show: bool = False, save: str = ""):
        irr = search(loan_amount, loan_terms, search_samples, client_min_rate,
                     client_max_rate, probability_of_default, loss_given_default)
        a = Amortization(loan_amount, irr, loan_terms)
        table = a.get_enriched_table(probability_of_default, loss_given_default)
        request = ""
        if show:
            if loan_marr < irr:
                request = "Approved"
                print("Loan request for", loan_amount, "due in", loan_terms, "terms with", a.annuity,
                      "fix payments and interest rate of", round(irr * 100, 2), "%:", request)
                print(table)
            else:
                request = "Rejected"
                print("Loan request for", loan_amount, "due in", loan_terms, "termns with", a.annuity,
                      "fix payments and interest rate of", round(irr * 100, 2), "%:", request)
                print(table)
        if save.endswith(".csv"):
            table.to_csv(save)

    @staticmethod
    def loan_request_cloud(sheet_id, show: bool = False):
        rate = RateValue(spreadsheet_id=sheet_id)
        request_value = RequestValue(spreadsheet_id=sheet_id)
        values = ConfigTable(spreadsheet_id=sheet_id)
        table_google = ResultTable(spreadsheet_id=sheet_id)
        irr = search(values.loan_amount, values.loan_terms, values.search_samples,
                     values.client_min_rate, values.client_max_rate, values.probability_of_default,
                     values.loss_given_default)
        a = Amortization(values.loan_amount, irr, values.loan_terms)
        table = a.get_enriched_table(values.probability_of_default, values.loss_given_default)
        rate.update(irr)
        request = ""


        if values.loan_marr < irr:
            request = "Approved"
            request_value.update(request)
            if show:
                print("Loan request for", values.loan_amount, "due in", values.loan_terms, "terms with", a.annuity,
                      "fix payments and interest rate of", round(irr * 100, 2), "%:", request)
                print(table)
        else:
            request = "Rejected"
            request_value.update(request)
            if show:
                print("Loan request for", values.loan_amount, "due in", values.loan_terms, "terms with", a.annuity,
                      "fix payments and interest rate of", round(irr * 100, 2), "%:", request)
                print(table)
        table = table.fillna("-")
        table_2 = [table.columns[:, ].values.astype(str).tolist()] + table.values.tolist()
        table_google.update(table_2)


if __name__ == "__main__":
    logging.basicConfig(level=EXPECTED_RATE_LOG_LEVEL)
    pd.options.display.float_format = '{:,.2f}'.format
    fire.Fire(Main)
