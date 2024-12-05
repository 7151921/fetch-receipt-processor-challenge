import logging

from app.core.exceptions import ReceiptNotFound, NoReceiptData, NoReceiptId
from app.data_store.receipt_data_store import ReceiptDataStore
from app.financial.rewards_calculation import RewardCalculation
from app.models.receipt import Receipt, ReceiptId, ReceiptRewards


class ReceiptService:
    def __init__(self):
        self.receipt_data_store: ReceiptDataStore = ReceiptDataStore()

    async def process_receipt(self, receipt: Receipt) -> ReceiptId:
        if not receipt:
            logging.error(f"No Receipt data provided.")
            raise NoReceiptData("No Receipt data provided.")
        stored_receipt_id: str = await self.receipt_data_store.store_receipt(receipt)
        if not stored_receipt_id:
            raise NoReceiptId("No Receipt id was generated.")
        logging.info(f"Receipt Id: {stored_receipt_id}")
        return ReceiptId(receipt_id=stored_receipt_id)

    async def calculate_points_by_receipt_id(self, receipt_id: ReceiptId) -> ReceiptRewards:
        if not receipt_id or not receipt_id.receipt_id:
            raise NoReceiptId("No Receipt id provided.")
        _id: str = receipt_id.receipt_id
        logging.info(f"Attempting to calculate Receipt Id points: {receipt_id}")
        receipt: Receipt = await self.receipt_data_store.get_receipt(_id)
        if not receipt:
            logging.error(f"Receipt not found: {_id}")
            raise ReceiptNotFound("Receipt not found")
        reward = RewardCalculation(receipt=receipt).calculate_reward().get_rewards()
        logging.info(f"Receipt Points: {reward} for Receipt Id: {_id}.")
        return ReceiptRewards(points=reward)
