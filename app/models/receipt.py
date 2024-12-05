from enum import Enum
from typing import List

from pydantic import BaseModel, Field


class ReceiptRegexPattern(Enum):
    PRICE_PATTERN = "^\\d+\\.\\d{2}$"
    SHORT_DESCRIPTION_PATTERN = "^[\\w\\s\\-]+$"
    RETAILER_PATTERN = "^[\\w\\s\\-&]+$"
    RECEIPT_ID_PATTERN = "^\\S+$"
    TIME_PATTERN = r"^(?:[01][0-9]|2[0-3]):[0-5][0-9]$"
    DATE_PATTERN = r"^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$"


class Item(BaseModel):
    shortDescription: str = Field(pattern=ReceiptRegexPattern.SHORT_DESCRIPTION_PATTERN.value)
    price: str = Field(pattern=ReceiptRegexPattern.PRICE_PATTERN.value)


class Receipt(BaseModel):
    retailer: str = Field(pattern=ReceiptRegexPattern.RETAILER_PATTERN.value)
    purchaseDate: str = Field(pattern=ReceiptRegexPattern.DATE_PATTERN.value)
    purchaseTime: str = Field(pattern=ReceiptRegexPattern.TIME_PATTERN.value)
    items: List[Item] = []
    total: str = Field(pattern=ReceiptRegexPattern.PRICE_PATTERN.value)


class ReceiptId(BaseModel):
    receipt_id: str = Field(pattern=ReceiptRegexPattern.RECEIPT_ID_PATTERN.value)


class ReceiptRewards(BaseModel):
    points: int = 0

