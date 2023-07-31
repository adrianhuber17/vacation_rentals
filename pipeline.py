from clean.rental_clean import clean_data
from transform.rentals_transform import transform_data


def pipeline():
    clean_data()
    transform_data()


if __name__ == "__main__":
    pipeline()
