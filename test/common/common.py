from uuid import UUID

import pytest

from app.models.receipt import Receipt

m_and_m = {
    "retailer": "M&M Corner Market",
    "purchaseDate": "2022-03-20",
    "purchaseTime": "14:33",
    "items": [
        {
            "shortDescription": "Gatorade",
            "price": "2.25"
        }, {
            "shortDescription": "Gatorade",
            "price": "2.25"
        }, {
            "shortDescription": "Gatorade",
            "price": "2.25"
        }, {
            "shortDescription": "Gatorade",
            "price": "2.25"
        }
    ],
    "total": "9.00"
}

target = {
    "retailer": "Target",
    "purchaseDate": "2022-01-01",
    "purchaseTime": "13:01",
    "items": [
        {
            "shortDescription": "Mountain Dew 12PK",
            "price": "6.49"
        }, {
            "shortDescription": "Emils Cheese Pizza",
            "price": "12.25"
        }, {
            "shortDescription": "Knorr Creamy Chicken",
            "price": "1.26"
        }, {
            "shortDescription": "Doritos Nacho Cheese",
            "price": "3.35"
        }, {
            "shortDescription": "   Klarbrunn 12-PK 12 FL OZ  ",
            "price": "12.00"
        }
    ],
    "total": "35.35"
}

target_with_bad_data = {
    "retailer": "Target",
    "purchaseDate": "2022-01-01",
    "purchaseTime": "13:01",
    "items": [
        {
            "shortDescription": "Mountain Dew 12PK",
            "price": "6.49"
        }, {
            "shortDescription": "Emils Cheese Pizza",
            "price": "12..25"
        }, {
            "shortDescription": "Knorr Creamy Chicken",
            "price": "1.26"
        }, {
            "shortDescription": "Doritos Nacho Cheese",
            "price": "3.35"
        }, {
            "shortDescription": "   Klarbrunn 12-PK 12 FL OZ  ",
            "price": "12.00"
        }
    ],
    "total": "35.35"
}


@pytest.fixture(scope="session")
def m_m_market_receipt():
    return Receipt(**m_and_m)


@pytest.fixture(scope="session")
def target_receipt():
    return Receipt(**target)


def is_uuid(uuid: str):
    try:
        UUID(uuid, version=4)
        return True
    except ValueError:
        return False
