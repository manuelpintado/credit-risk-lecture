from typing import Dict, List, Optional, Union

from utils import get_google_sheet_service


class GoogleSheetWrapper:

    def __init__(self, spreadsheet_id: str, sheet_name: str):
        self.spreadsheet_id = spreadsheet_id
        self.sheet_name = sheet_name
        self.sheet_service = get_google_sheet_service().values()

    def update_values(self, values: Union[str, List], from_col: str, from_row: Union[str, int],
                      to_col: str, to_row: Union[str, int]):
        if from_col == to_col and str(from_row) == str(to_row):
            return self.update_value(value=values, col=from_col, row=from_row)
        sheet_range = f"{self.sheet_name}!{from_col}{from_row}:{to_col}{to_row}"
        body = {
            "values": values
        }
        target = self.sheet_service.update(spreadsheetId=self.spreadsheet_id, range=sheet_range,
                                           valueInputOption="RAW", body=body)
        return target.execute()

    def update_value(self, value: str, col: str, row: Union[str, int]):
        sheet_range = f"{self.sheet_name}!{col}{row}"
        body = {
            "values": [[value]]
        }
        target = self.sheet_service.update(spreadsheetId=self.spreadsheet_id, range=sheet_range,
                                           valueInputOption="RAW", body=body)
        return target.execute()

    def get_value(self, col: str, row: Union[str, int]):
        sheet_range = f"{self.sheet_name}!{col}{row}"
        target = self.sheet_service.get(spreadsheetId=self.spreadsheet_id, range=sheet_range)
        request = target.execute()['values']
        (request,), = request
        return request

    def get_values(self, from_col: str, from_row: Union[str, int], to_col: str, to_row: Union[str, int]):
        if from_col == to_col and str(from_row) == str(to_row):
            return self.get_value(col=from_col, row=from_row)
        sheet_range = f"{self.sheet_name}!{from_col}{from_row}:{to_col}{to_row}"
        target = self.sheet_service.get(spreadsheetId=self.spreadsheet_id, range=sheet_range)
        request = target.execute()['values']
        if from_row == to_row or from_col == to_col:
            flat_list = []
            for sublist in request:
                for item in sublist:
                    flat_list.append(item)
            return flat_list
        return request


class ConfigTable:
    RESOURCE_ID = "TABLE_CONFIG"

    def __init__(self, spreadsheet_id: str):
        self.spreadsheet_id = spreadsheet_id
        self.metadata = GoogleSheetWrapper(spreadsheet_id=self.spreadsheet_id,
                                           sheet_name="METADATA").get_values(from_col="E", from_row=3,
                                                                             to_col="H", to_row=3)
        self.sheet = GoogleSheetWrapper(spreadsheet_id=self.spreadsheet_id, sheet_name="CONFIG")
        self.table = dict(self.sheet.get_values(from_col=self.metadata[0], from_row=self.metadata[1],
                                                to_col=self.metadata[2], to_row=self.metadata[3]))

    @property
    def probability_of_default(self):
        PD = self.table['PROB_OF_DEFAULT']
        return float(PD)

    @property
    def loss_given_default(self):
        LGD = self.table['LGD']
        return float(LGD)

    @property
    def loan_amount(self):
        LA = self.table['LOAN_AMOUNT']
        return float(LA)

    @property
    def loan_terms(self):
        LT = self.table['LOAN_TERMS']
        return int(LT)

    @property
    def loan_marr(self):
        LM = self.table['LOAN_MARR']
        return float(LM)

    @property
    def client_min_rate(self):
        mn = self.table['CLIENT_MIN_RATE']
        return float(mn)

    @property
    def client_max_rate(self):
        mx = self.table['CLIENT_MAX_RATE']
        return float(mx)

    @property
    def search_samples(self):
        samples = self.table['SEARCH_SAMPLES']
        return int(samples)


class RateValue:
    RESOURCE_ID = "VALUE_EXPECTED_RATE"

    def __init__(self, spreadsheet_id: str):
        self.spreadsheet_id = spreadsheet_id
        self.metadata = GoogleSheetWrapper(spreadsheet_id=self.spreadsheet_id, sheet_name="METADATA")
        self.table = self.metadata.get_values(from_col="E", from_row=4, to_col="H", to_row=4)
        self.sheet = GoogleSheetWrapper(spreadsheet_id=self.spreadsheet_id, sheet_name="RATE")

    def update(self, value: str):
        self.sheet.update_values(value, from_col=self.table[0], from_row=self.table[1],
                                 to_col=self.table[2], to_row=self.table[3])


class RequestValue:
    RESOURCE_ID = "VALUE_REQUEST"

    def __init__(self, spreadsheet_id: str):
        self.spreadsheet_id = spreadsheet_id
        self.metadata = GoogleSheetWrapper(spreadsheet_id=self.spreadsheet_id, sheet_name="METADATA")
        self.table = self.metadata.get_values(from_col="E", from_row=5, to_col="H", to_row=5)
        self.sheet = GoogleSheetWrapper(spreadsheet_id=self.spreadsheet_id, sheet_name="RATE")

    def update(self, value: str):
        self.sheet.update_values(value, from_col=self.table[0], from_row=self.table[1],
                                 to_col=self.table[2], to_row=self.table[3])


class ResultTable:
    RESOURCE_ID = "TABLE_RESULT"

    def __init__(self, spreadsheet_id: str):
        self.n = ConfigTable(spreadsheet_id=spreadsheet_id).loan_terms
        self.spreadsheet_id = spreadsheet_id
        self.metadata = GoogleSheetWrapper(spreadsheet_id=self.spreadsheet_id, sheet_name="METADATA")
        self.table = self.metadata.get_values(from_col="E", from_row=6, to_col="H", to_row=6)
        self.sheet = GoogleSheetWrapper(spreadsheet_id=self.spreadsheet_id, sheet_name="RESULT")
        self.table[3] = self.n+2

    def update(self, values: List):
        self.sheet.update_values(values, from_col=self.table[0], from_row=self.table[1],
                                 to_col=self.table[2], to_row=self.table[3])
