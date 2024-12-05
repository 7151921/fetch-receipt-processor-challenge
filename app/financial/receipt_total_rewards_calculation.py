import logging
from decimal import Decimal

from app.financial.abstract_rewards_calulation import AbstractRewardsCalculation

DEFAULT_MULTIPLE: Decimal = Decimal('0.25')
DEFAULT_ROUND_DOLLAR_REWARD = 50
DEFAULT_MULTIPLE_DOLLAR_REWARD = 25


class ReceiptTotalRewardsCalculation(AbstractRewardsCalculation):
    def __init__(self, receipt_total: str, multiple: Decimal = DEFAULT_MULTIPLE,
                 round_dollar_reward: int = DEFAULT_ROUND_DOLLAR_REWARD,
                 multiple_dollar_reward: int = DEFAULT_MULTIPLE_DOLLAR_REWARD):
        self.receipt_total: str = receipt_total
        self.multiple: Decimal = multiple
        self.round_dollar_reward: int = round_dollar_reward
        self.multiple_dollar_reward: int = multiple_dollar_reward
        self.rewards: int = 0

    def calculate_reward(self):
        logging.info("Calculating receipt total rewards...")
        self.__calculate_total_round_dollar_rewards()
        self.__calculate_total_is_multiple_reward()
        return self

    def get_rewards(self) -> int:
        logging.info(f"Receipt Total rewards total: {self.rewards}")
        return self.rewards

    def __calculate_total_round_dollar_rewards(self):
        if self.receipt_total.endswith(".00"):
            logging.debug(f"Receipt ends with .00 adding {self.round_dollar_reward}")
            self.rewards += self.round_dollar_reward

    def __calculate_total_is_multiple_reward(self):
        receipt_total: Decimal = Decimal(self.receipt_total)
        if receipt_total % self.multiple == 0:
            logging.debug(f"Receipt total is multiple of {self.multiple} adding {self.round_dollar_reward}")
            self.rewards += self.multiple_dollar_reward
