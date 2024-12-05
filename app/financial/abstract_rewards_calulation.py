from abc import ABC, abstractmethod


class AbstractRewardsCalculation(ABC):

    @abstractmethod
    def calculate_reward(self):
        raise NotImplementedError

    @abstractmethod
    def get_rewards(self):
        return NotImplementedError

