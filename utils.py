COLUMNS = [
    "name",
    "res_num",
    "created",
    "type",
    "status",
    "arrive",
    "nights",
    "depart",
    "guests",
    "room_rent",
    "owner_commission",
    "management_commission",
    "action",
]

dtypes_to_cast = {
    "name": object,
    "res_num": "int64",
    "created": "datetime64",
    "type": object,
    "status": object,
    "arrive": "datetime64",
    "nights": "int64",
    "depart": "datetime64",
    "guests": object,
    "room_rent": "float64",
    "owner_commission": "float64",
    "management_commission": "float64",
    "action": object,
}

COLUMNS_TO_DROP = [
    "Unnamed: 0",
    "name",
    "res_num",
    "created",
    "status",
    "depart",
    "guests",
    "action",
]
