import logging
from datetime import datetime, date

from app.financial.abstract_rewards_calulation import AbstractRewardsCalculation

DEFAULT_ODD_DAY_REWARD: int = 6
DEFAULT_DAY_GROUP: int = 2
DEFAULT_DATE_FORMAT: str = '%Y-%m-%d'


class PurchaseDayRewardsCalculation(AbstractRewardsCalculation):
    def __init__(self, purchase_date: str, odd_day_reward: int = DEFAULT_ODD_DAY_REWARD,
                 day_group: int = DEFAULT_DAY_GROUP, date_format: str = DEFAULT_DATE_FORMAT):
        self.purchase_date = purchase_date
        self.odd_day_reward = odd_day_reward
        self.day_group = day_group
        self.date_format = date_format
        self.odd_remainder = 1
        self.rewards = 0

    def calculate_reward(self):
        logging.info("Calculating Purchase Day rewards...")
        self.__calculate_odd_day_rewards()
        return self

    def get_rewards(self):
        logging.info(f"Purchase Day reward total: {self.rewards}")
        return self.rewards

    def __calculate_odd_day_rewards(self):
        logging.info("Calculating Odd Day rewards.")
        self.__calculate_day_group_rewards(day_group=self.day_group, remainder=self.odd_remainder,
                                           reward=self.odd_day_reward)

    def __calculate_day_group_rewards(self, day_group: int, remainder: int, reward: int):
        purchase_date: date = self.__convert_to_date_format()
        if purchase_date.day % day_group == remainder:
            logging.info(f"Criteria met adding {reward}")
            self.rewards += reward

    def __convert_to_date_format(self) -> date:
        return datetime.strptime(self.purchase_date, self.date_format).date()
