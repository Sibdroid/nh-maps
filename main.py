import pandas as pd
import numpy as np


def remove_nans(values: list) -> list:
    return [i for i in values if not pd.isna(i)]


def xlsx_to_data(path: str) -> pd.DataFrame:
    df = pd.read_excel(path, header=0)
    candidates = []
    for column in df.columns:
        column_data = df[column].tolist()
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
# carroll - fails because no nan
# cheshire - works kind of
# coos - fails because no nan
# grafton - fails because no nan
# hillsborough - fails because no nan
# merrimack - fails because no nan
# rockingham - fails because no nan
# strafford - fails because no nan
# sullivan - works kind of
