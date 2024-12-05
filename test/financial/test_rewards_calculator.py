from app.financial.rewards_calculation import RewardCalculation
import pytest

from app.models.receipt import Receipt
from test.common.common import target_receipt, m_m_market_receipt


@pytest.fixture
def reward_calculator_target(target_receipt: Receipt):
    return RewardCalculation(receipt=target_receipt)


@pytest.fixture
def reward_calculator_m_m_market_receipt(m_m_market_receipt: Receipt):
    return RewardCalculation(receipt=m_m_market_receipt)


def test_reward_calculation_data_type(reward_calculator_m_m_market_receipt: RewardCalculation):
    assert isinstance(reward_calculator_m_m_market_receipt.calculate_reward(), RewardCalculation)


def test_get_reward_data_type(reward_calculator_m_m_market_receipt: RewardCalculation):
    assert isinstance(reward_calculator_m_m_market_receipt.get_rewards(), int)


def test_get_reward_no_calculation(reward_calculator_m_m_market_receipt: RewardCalculation):
    assert reward_calculator_m_m_market_receipt.get_rewards() == 0


def test_m_m_rewards_calculator(reward_calculator_m_m_market_receipt: RewardCalculation):
    assert reward_calculator_m_m_market_receipt.calculate_reward().get_rewards() == 109


def test_target_rewards_calculator(reward_calculator_target: RewardCalculation):
    assert reward_calculator_target.calculate_reward().get_rewards() == 28
