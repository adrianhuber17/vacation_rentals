import pandas as pd
import utils as U


def clean_data():
    """
    Clean raw dataframe and output a clean dataframe
    1) renames columns
    2) removes special characters
    3) casts data types for all columns
    4) clean columns (lower naming, etc)
    """
    rentals_raw = pd.read_csv("raw/rentals_raw.csv")

    # rename columns
    rentals_raw = rename_columns(rentals_raw)

    # remove special characters
    rentals_raw = remove_special_chars(rentals_raw)

    # cast types to columns
    rentals_raw = cast_dtypes(rentals_raw)

    # rename dataframe to clean
    rentals_clean = rentals_raw.to_csv("clean/rentals_clean.csv")


def rename_columns(rentals_raw):
    """
    rename columns in raw dataframe
    """
    curr_col_names = list(rentals_raw.columns)
    new_col_names = U.COLUMNS

    column_mapping = {
        old_name: new_name for old_name, new_name in zip(curr_col_names, new_col_names)
    }

    rentals_raw.rename(columns=column_mapping, inplace=True)

    return rentals_raw


def cast_dtypes(rentals_raw):
    """
    cast dtypes to all columns
    """
    rentals_raw = rentals_raw.astype(U.dtypes_to_cast)

    return rentals_raw


def clean_columns(rentals_raw):
    return rentals_raw


def remove_special_chars(rentals_raw):
    """
    remove special characters in currency columns
    """
    cols_to_fix = ["room_rent", "owner_commission", "management_commission"]

    for cols in cols_to_fix:
        rentals_raw[cols] = rentals_raw[cols].str.replace("$", "", regex=True)
        rentals_raw[cols] = rentals_raw[cols].str.replace(",", "", regex=True)

    return rentals_raw
