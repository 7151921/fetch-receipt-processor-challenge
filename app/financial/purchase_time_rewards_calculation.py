import logging
from datetime import datetime, time

from app.financial.abstract_rewards_calulation import AbstractRewardsCalculation

TIME_FORMAT: str = "%H:%M"
DEFAULT_BEGIN_REWARD_TIME: int = 14  # 2:00pm
DEFAULT_END_REWARD_TIME: int = 16  # 4:00pm
DEFAULT_BETWEEN_TIME_REWARD: int = 10


class PurchaseTimeRewardsCalculation(AbstractRewardsCalculation):
    def __init__(self, purchase_time: str, begin_reward_time: int = DEFAULT_BEGIN_REWARD_TIME,
                 end_reward_time: int = DEFAULT_END_REWARD_TIME,
                 between_time_reward: int = DEFAULT_BETWEEN_TIME_REWARD):
        self.purchase_time: time = datetime.strptime(purchase_time, TIME_FORMAT).time()
        self.begin_reward_time: time = time(begin_reward_time, 0)
        self.end_reward_time: time = time(end_reward_time, 0)
        self.between_time_reward: int = between_time_reward
        self.rewards: int = 0

    def calculate_reward(self):
        logging.info("Calculating purchase time rewards...")
        self.__calculate_reward_between_reward_time()
        return self

    def get_rewards(self) -> int:
        logging.info(f"Purchase time rewards total: {self.rewards}")
        return self.rewards

    def __calculate_reward_between_reward_time(self):
        if self.__is_between_reward_time():
            logging.info(f"The purchase time is between the reward window adding {self.between_time_reward}")
            self.rewards += self.between_time_reward

    def __is_between_reward_time(self) -> bool:
        return self.begin_reward_time < self.purchase_time < self.end_reward_time
