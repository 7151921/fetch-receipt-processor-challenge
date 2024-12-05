import logging
import math
from decimal import Decimal
from typing import List

from app.financial.abstract_rewards_calulation import AbstractRewardsCalculation
from app.models.receipt import Item

DEFAULT_GROUP_SIZE: int = 2
DEFAULT_REWARDS_PER_GROUP: int = 5
DEFAULT_PRICE_MULTIPLIER: Decimal = Decimal('0.2')
DEFAULT_SHORT_DESCRIPTION_GROUP: int = 3


class ItemRewardsCalculation(AbstractRewardsCalculation):
    def __init__(self, items: List[Item], group_size: int = DEFAULT_GROUP_SIZE,
                 reward_per_group: int = DEFAULT_REWARDS_PER_GROUP,
                 price_multiplier: Decimal = DEFAULT_PRICE_MULTIPLIER,
                 short_description_group: int = DEFAULT_SHORT_DESCRIPTION_GROUP):
        self.items: List[Item] = items
        self.group_size: int = group_size
        self.reward_per_group: int = reward_per_group
        self.price_multiplier: Decimal = price_multiplier
        self.short_description_group: int = short_description_group
        self.rewards = 0

    def calculate_reward(self):
        logging.info("Calculating Item rewards.")
        self.__calculate_grouping_reward()
        self.__calculate_trimmed_item_description_reward()
        return self

    def get_rewards(self) -> int:
        logging.info(f"Item rewards total: {self.rewards}.")
        return self.rewards

    def __calculate_grouping_reward(self):
        logging.info("Calculating Grouping Reward.")
        number_of_items: int = len(self.items)
        reward = math.floor(number_of_items / self.group_size) * self.reward_per_group
        logging.info(f"Grouping reward: {reward}.")
        self.rewards += reward

    def __calculate_trimmed_item_description_reward(self):
        logging.info("Calculating Trimmed Item Description Reward.")
        initial_rewards = self.rewards
        for item in self.items:
            stripped_short_description: str = item.shortDescription.strip()
            count_short_description: int = len(stripped_short_description)

            if count_short_description % self.short_description_group == 0:
                item_price_with_multiplier: Decimal = Decimal(item.price) * self.price_multiplier
                self.rewards += math.ceil(item_price_with_multiplier)
        logging.info(f"Trimmed Item Description reward: {self.rewards - initial_rewards}.")