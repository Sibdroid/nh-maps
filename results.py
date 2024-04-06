import pandas as pd
def main() -> None:
    xls = pd.ExcelFile("full-saved-again-full-saved.xlsx")
    df = pd.read_excel(xls, "State Senate", header=0)
    for i in range(1, 25):
        small_df = df[df["District"] == i]
        small_df = small_df.iloc[:, 1:].iloc[:, :-1]
        haley = sum(small_df["Haley, Nikki (r)"])
        trump = sum(small_df["Trump, Donald J. (r)"])
        total = small_df.to_numpy().sum()
        print(f"District: {i}")
        if trump > haley:
            print(f"Trump: {round(trump / total * 100, 3)}")
        else:
            print(f"Haley: {round(haley / total * 100, 3)}")
        print("")


if __name__ == "__main__":
    main()