import pandas as pd
import numpy as np
import os


def remove_nans(values: list) -> list:
    return [i for i in values if not pd.isna(i)]


def xlsx_to_data(path: str) -> pd.DataFrame:
    df = pd.read_excel(path, header=0)
    candidates = []
    for column in df.columns:
        column_data = df[column].tolist()
        if pd.isna(column_data[-1]):
            column_data = column_data[:-1]
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
    df = df.apply(lambda x: pd.to_numeric(x, errors='coerce')).dropna()
    df = df.map(lambda x: int(x))
    df = df.T
    return df


def main() -> None:
    files = [f for f in os.listdir(".") if os.path.isfile(f)]
    for file in files:
        if file.endswith(".xlsx"):
            data = xlsx_to_data(file)
            print(data.columns.tolist())


if __name__ == "__main__":
    main()
# belknap - made for this
# carroll - works kind of
# cheshire - works kind of
# coos - works kind of
# grafton - works kind of
# hillsborough - works
# merrimack - works
# rockingham - works
# strafford - works
# sullivan - works kind of
