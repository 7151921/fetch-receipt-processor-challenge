import json
import logging
import uuid
from typing import Optional, Dict, Any

from app.core.exceptions import NoReceiptData
from app.models.receipt import Receipt


class ReceiptDataStore:
    def __init__(self):
        self.store: Dict[str, Receipt] = {}

    async def store_receipt(self, data: Receipt) -> str:
        if data is None:
            raise NoReceiptData("Receipt data cannot be None")
        logging.info("Generating UUID.")
        receipt_id = str(uuid.uuid4())
        self.store[receipt_id] = data
        logging.debug(f"Storing receipt: {await self.__json_handler(data)}")
        logging.debug(f"Current Data Store: {await self.__store_to_json()}.")
        return receipt_id

    async def get_receipt(self, receipt_id: str) -> Optional[Receipt]:
        logging.debug(f"Getting receipt {receipt_id}")
        return self.store.get(receipt_id)

    async def update_receipt(self, receipt_id: str, data: Receipt) -> bool:
        if data is None:
            raise ValueError("Receipt data cannot be None")
        receipt_updated = False
        if receipt_id in self.store:
            logging.debug(f"Updating receipt {receipt_id}, with data: {await self.__receipt_to_json(data)}.")
            self.store[receipt_id] = data
            receipt_updated = True
        logging.debug(f"Receipt was updated: {receipt_updated}.")
        return receipt_updated

    async def delete_receipt(self, receipt_id: str) -> bool:
        receipt_deleted = False
        if receipt_id in self.store:
            logging.debug(f"Deleting receipt {receipt_id}.")
            del self.store[receipt_id]
            receipt_deleted = True
        logging.debug(f"Receipt was deleted: {receipt_deleted}.")
        return receipt_deleted

    async def list_all_receipts(self) -> Dict[str, Receipt]:
        return self.store

    async def __store_to_json(self):
        return await self.__json_handler(self.store)

    async def __receipt_to_json(self, data: Receipt) -> str:
        return await self.__json_handler(data)

    @staticmethod
    async def __json_handler(data) -> str:
        return json.dumps(data,
                          default=lambda o: o.__dict__,
                          sort_keys=True,
                          indent=4)
