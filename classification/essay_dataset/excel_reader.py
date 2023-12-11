# import pandas lib as pd
import pandas as pd
import os

try:
    file = os.path.join(
        os.pardir,
        os.pardir,
        "data",
        "FDE_final_alle Ratings_mit Legende Spalten_071123.xlsx",
    )
    # read by default 1st sheet of an excel file
    df = pd.read_excel(file).dropna()

    print(df)
except FileNotFoundError as e:
    print(f"no file at: {file}")
    raise e
