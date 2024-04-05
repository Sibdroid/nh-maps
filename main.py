import pandas as pd
import numpy as np


def remove_nans(values: list) -> list:
    return [i for i in values if not pd.isna(i)]


def xlsx_to_data(path: str) -> pd.DataFrame:
    df = pd.read_excel(path, header=0)
    candidates = []
    for column in df.columns:
        column_data = df[column].tolist()
        if np.nan not in column_data:
            if "TOTALS" in column_data:
                column_data.insert(column_data.index("TOTALS")+1, np.nan)
            else:
                second_string = [i for i in column_data
                                 if isinstance(i, str)][1]
                column_data.insert(column_data.index(second_string), np.nan)
        nan_index = column_data.index(np.nan)
        first_candidate = remove_nans(column_data[0:nan_index])
        second_candidate = remove_nans(column_data[nan_index+1:])
        for candidate in [first_candidate, second_candidate]:
            if len(candidate) > 1:
                candidates += [candidate]
    min_length = min([len(candidate) for candidate in candidates])
    candidates = [candidate for candidate in candidates if
                  len(candidate) == min_length]
    municipalities = candidates[0]
    candidates = candidates[1:]
    df = pd.DataFrame(candidates, columns=municipalities)
    df = df.set_index(df.columns[0])
    df.index.names = ["Candidate"]
    return df


print(xlsx_to_data("2024-pp-republican-sullivan_1.xlsx").to_string())

# belknap - made for this
# carroll - works kind of
# cheshire - works kind of
# coos - works kind of
# grafton - works kind of
# hillsborough - fails for weird reason, idk
# merrimack - fails for weird reason, idk
# rockingham - fails for weird reason, idk
# strafford - fails for weird reason, idk
# sullivan - works kind of
