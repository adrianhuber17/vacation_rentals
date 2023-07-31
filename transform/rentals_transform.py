import pandas as pd
import utils as U


def transform_data():
    """
    Transforms clean dataframe and output a trasform dataframe
    1) drops columns that are not needed
    """
    rentals_transform = pd.read_csv("clean/rentals_clean.csv")

    rentals_transform = drop_columns(rentals_transform)

    rentals_transform = rentals_transform.to_csv("transform/rentals_transform.csv")


def drop_columns(rentals_transform):
    rentals_transform = rentals_transform.drop(columns=U.COLUMNS_TO_DROP).reset_index(
        drop=True
    )

    return rentals_transform
