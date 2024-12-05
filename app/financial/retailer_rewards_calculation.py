import logging
from typing import Callable

from app.financial.abstract_rewards_calulation import AbstractRewardsCalculation


class RetailerRewardsCalculation(AbstractRewardsCalculation):
    def __init__(self, retailer: str):
        self.retailer: str = retailer
        self.rewards: int = 0

    def calculate_reward(self):
        logging.info("Calculating Retailer rewards...")
        self.__calculate_alpha_reward()
        self.__calculate_numeric_reward()
        return self

    def get_rewards(self):
        logging.info(f"Retailer rewards total: {self.rewards}")
        return self.rewards

    def __calculate_alpha_reward(self):
        logging.info("Calculating Alpha Reward...")
        self.rewards += self.__calculate_conditional_reward(self.retailer, self.__is_alpha)

    def __calculate_numeric_reward(self):
        logging.info("Calculating Numeric Reward...")
        self.rewards += self.__calculate_conditional_reward(self.retailer, self.__is_numeric)

    @staticmethod
    def __calculate_conditional_reward(string: str, conditional_callable: Callable[[str], bool]) -> int:
        count = 0
        for char in string:
            if conditional_callable(char):
                count += 1
        return count

    # Python does not have a character data type.
    @staticmethod
    def __is_alpha(char: str) -> bool:
        return char.isalpha()

    @staticmethod
    def __is_numeric(char: str) -> bool:
        return char.isnumeric()
