from typing import List

from app.financial.abstract_rewards_calulation import AbstractRewardsCalculation
from app.financial.items_rewards_calculation import ItemRewardsCalculation
from app.financial.purchase_day_rewards_calculation import PurchaseDayRewardsCalculation
from app.financial.purchase_time_rewards_calculation import PurchaseTimeRewardsCalculation
from app.financial.receipt_total_rewards_calculation import ReceiptTotalRewardsCalculation
from app.financial.retailer_rewards_calculation import RetailerRewardsCalculation
from app.models.receipt import Receipt


class RewardCalculation(AbstractRewardsCalculation):
    def __init__(self, receipt: Receipt):
        self.receipt = receipt
        self.rewards = 0

    def calculate_reward(self):
        reward_calculators: List[AbstractRewardsCalculation] = [
            ReceiptTotalRewardsCalculation(receipt_total=self.receipt.total),
            RetailerRewardsCalculation(retailer=self.receipt.retailer),
            PurchaseTimeRewardsCalculation(purchase_time=self.receipt.purchaseTime),
            PurchaseDayRewardsCalculation(purchase_date=self.receipt.purchaseDate),
            ItemRewardsCalculation(items=self.receipt.items),
        ]
        self.rewards = sum(calculator.calculate_reward().get_rewards() for calculator in reward_calculators)
        return self

    def get_rewards(self) -> int:
        return self.rewards


